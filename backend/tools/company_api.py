import os, functools, time, random, logging
from typing import Optional, Dict, List, Union
from datetime import datetime, timedelta
import httpx
from config import settings
from utils.api_cache import with_persistent_cache

log = logging.getLogger(__name__)

# =============================================================================
# REAL EXPLORIUM API IMPLEMENTATION
# =============================================================================

EXPLORIUM_BASE = "https://api.explorium.ai/v1"
HEADERS = lambda: {"API_KEY": settings.EXPLORIUM_API_KEY or "", "Content-Type": "application/json"}
LOOKBACK_DAYS = 90
TIMESTAMP_FROM = lambda: (datetime.utcnow() - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def with_retry(max_retries=2, backoff=1.0):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return fn(*args, **kwargs)
                except httpx.HTTPStatusError as e:
                    resp = getattr(e, 'response', None)
                    if resp is not None:
                        if resp.status_code == 429:
                            time.sleep(backoff * (attempt + 1))
                            continue
                        if resp.status_code in (401, 403):
                            log.error(f"API auth failed: {fn.__name__} — check .env. {resp.text}")
                            return None
                        log.error(f"Explorium API HTTP {resp.status_code} in {fn.__name__}: {resp.text}")
                    return None
                except (httpx.TimeoutException, httpx.RequestError) as e:
                    log.error(f"Explorium network error in {fn.__name__}: {e}")
                    return None
            return None
        return wrapper
    return decorator


@with_persistent_cache(ttl_days=30)
@with_retry()
def _real_match_business(name: str, website: str = None) -> Optional[str]:
    """Step 1: Resolve a company name/website to an Explorium business_id."""
    payload: dict = {"name": name}
    if website:
        payload["website"] = website
    response = httpx.post(
        f"{EXPLORIUM_BASE}/businesses/match",
        json={"businesses_to_match": [payload]},
        headers=HEADERS(), timeout=15.0
    )
    response.raise_for_status()
    matches = response.json().get("matched_businesses", [])
    if matches:
        return matches[0].get("business_id")
    return None


@with_persistent_cache(ttl_days=30)
@with_retry()
def _real_search_companies(query_str: str = "", filters: dict = None) -> list[dict]:
    """Fetch businesses from Explorium."""
    api_filters = {"has_website": {"value": True}}
    if filters:
        api_filters.update(filters)
        
    response = httpx.post(
        f"{EXPLORIUM_BASE}/businesses",
        json={
            "mode": "full",
            "page_size": 1,
            "size": 1,
            "filters": api_filters
        },
        headers=HEADERS(), timeout=45.0
    )
    response.raise_for_status()
    companies = response.json().get("data", [])
    return [
        {
            "name": c.get("name"),
            "industry": c.get("industry"),
            "description": c.get("short_description") or c.get("description"),
            "employee_count": c.get("employee_count"),
            "website": c.get("website"),
            "headquarters": c.get("hq_location") or c.get("headquarters"),
            "founded_year": c.get("founded_year"),
            "explorium_id": c.get("business_id"),
        }
        for c in companies
    ]


@with_persistent_cache(ttl_days=30)
@with_retry()
def _real_enrich_company(business_id: str) -> Optional[dict]:
    if not business_id:
        return None
    response = httpx.post(
        f"{EXPLORIUM_BASE}/businesses",
        json={
            "mode": "full",
            "page_size": 1,
            "size": 1,
            "filters": {
                "business_id": {"values": [business_id]}
            }
        },
        headers=HEADERS(), timeout=15.0
    )
    response.raise_for_status()
    data = response.json().get("data", [])
    return data[0] if data else None


@with_persistent_cache(ttl_days=30)
@with_retry()
def _real_get_business_events(business_id: str, event_types: list[str]) -> list[dict]:
    if not business_id:
        return []
    response = httpx.post(
        f"{EXPLORIUM_BASE}/businesses/events",
        json={
            "business_ids": [business_id],
            "event_types": event_types,
            "timestamp_from": TIMESTAMP_FROM()
        },
        headers=HEADERS(), timeout=15.0
    )
    response.raise_for_status()
    return response.json().get("events", [])


@with_persistent_cache(ttl_days=30)
@with_retry()
def _real_fetch_prospects(business_id: str, job_levels: list = None, job_departments: list = None) -> list[dict]:
    filters = {"business_id": {"values": [business_id]}}
    if job_levels:
        filters["job_level"] = {"values": job_levels}
    if job_departments:
        filters["job_department"] = {"values": job_departments}
    
    response = httpx.post(
        f"{EXPLORIUM_BASE}/prospects",
        json={
            "mode": "full",
            "page_size": 3,
            "filters": filters
        },
        headers=HEADERS(), timeout=30.0
    )
    response.raise_for_status()
    prospects = response.json().get("data", [])
    return prospects


@with_persistent_cache(ttl_days=30)
@with_retry()
def _real_enrich_contact(prospect_id: str) -> Optional[dict]:
    response = httpx.post(
        f"{EXPLORIUM_BASE}/prospects/contacts_information/enrich",
        json={
            "prospect_id": prospect_id,
            "parameters": {
              "contact_types": ["email"]
            }
        },
        headers=HEADERS(), timeout=15.0
    )
    response.raise_for_status()
    return response.json().get("data")


@with_persistent_cache(ttl_days=30)
@with_retry()
def _real_bulk_enrich_contacts(prospect_ids: list[str]) -> list[dict]:
    if not prospect_ids:
        return []
    response = httpx.post(
        f"{EXPLORIUM_BASE}/prospects/contacts_information/bulk_enrich",
        json={"prospect_ids": prospect_ids[:50]}, # max 50 per docs
        headers=HEADERS(), timeout=20.0
    )
    response.raise_for_status()
    return response.json().get("data", [])


def get_leadership_changes(events: list[dict]) -> list[dict]:
    target_events = [e for e in (events or []) if e.get("event_name") == "employee_joined_company"]
    return [
        {
            "name": e.get("full_name"),
            "role": e.get("job_role_title"),
            "department": e.get("job_department"),
            "linkedin_url": e.get("linkedin_url"),
            "event_time": e.get("event_time"),
        }
        for e in target_events
    ]


def get_hiring_signals(events: list[dict]) -> list[str]:
    hiring_event_types = [
        "hiring_in_sales_department",
        "hiring_in_engineering_department",
        "hiring_in_marketing_department",
        "hiring_in_operations_department",
        "hiring_in_human_resources_department",
        "increase_in_sales_department",
        "increase_in_engineering_department",
    ]
    target_events = [e for e in (events or []) if e.get("event_name") in hiring_event_types]
    signals = []
    for e in target_events:
        dept = e.get("department") or e.get("event_name", "")
        titles = e.get("job_titles", [])
        count = e.get("job_count", "")
        if titles:
            signals.append(f"Hiring in {dept}: {', '.join(titles[:3])} ({count} roles)")
        else:
            signals.append(f"Workforce increase in {dept}")
    return signals


def get_funding_info(events: list[dict]) -> Optional[dict]:
    target_events = [e for e in (events or []) if e.get("event_name") in ["new_funding_round", "new_investment", "ipo_announcement"]]
    if not target_events:
        return None
    e = target_events[0]
    return {
        "funding_round": e.get("funding_round") or e.get("event_name"),
        "funding_amount": e.get("funding_amount"),
        "funding_date": e.get("founding_date") or e.get("event_time"),
        "investors": e.get("investors", []),
        "event_type": e.get("event_name"),
    }


def get_strategic_events(events: list[dict]) -> list[dict]:
    target_events = [e for e in (events or []) if e.get("event_name") in ["merger_and_acquisitions", "new_product", "new_partnership", "cost_cutting"]]
    return [
        {
            "type": e.get("event_name"),
            "title": e.get("title") or e.get("product_name"),
            "description": e.get("description") or e.get("snippet"),
            "event_time": e.get("event_time"),
        }
        for e in target_events
    ]


# =============================================================================
# MOCK IMPLEMENTATIONS
# =============================================================================

_MOCK_COMPANIES = [
    {
        "name": "TechFlow AI",
        "industry": "Software",
        "description": "Workflow automation for engineering teams.",
        "employee_count": 120,
        "website": "https://techflow.ai",
        "headquarters": "San Francisco, CA",
        "founded_year": 2019,
        "explorium_id": "mock-biz-001",
    },
    {
        "name": "CyberShield",
        "industry": "Cybersecurity",
        "description": "AI-powered threat detection and response platform.",
        "employee_count": 250,
        "website": "https://cybershield.net",
        "headquarters": "Boston, MA",
        "founded_year": 2017,
        "explorium_id": "mock-biz-002",
    },
    {
        "name": "GreenGrid",
        "industry": "CleanTech",
        "description": "Smart grid management software for utilities.",
        "employee_count": 45,
        "website": "https://greengrid.io",
        "headquarters": "Austin, TX",
        "founded_year": 2021,
        "explorium_id": "mock-biz-003",
    },
    {
        "name": "DataPulse",
        "industry": "Analytics",
        "description": "Real-time data pipeline orchestration for mid-market.",
        "employee_count": 80,
        "website": "https://datapulse.io",
        "headquarters": "New York, NY",
        "founded_year": 2020,
        "explorium_id": "mock-biz-004",
    },
    {
        "name": "ScaleOps",
        "industry": "DevOps",
        "description": "Kubernetes cost optimization and auto-scaling platform.",
        "employee_count": 60,
        "website": "https://scaleops.com",
        "headquarters": "Seattle, WA",
        "founded_year": 2022,
        "explorium_id": "mock-biz-005",
    },
]

_MOCK_EVENTS = {
    "mock-biz-001": {
        "hiring": [
            {"event_name": "hiring_in_sales_department", "job_titles": ["VP Sales", "Account Executive"], "job_count": 5, "department": "Sales"},
            {"event_name": "hiring_in_engineering_department", "job_titles": ["Senior Backend Engineer"], "job_count": 3, "department": "Engineering"},
        ],
        "funding": [{"event_name": "new_funding_round", "funding_round": "Series B", "funding_amount": 25000000, "event_time": "2024-03-01", "investors": ["Sequoia", "a16z"]}],
        "leadership": [{"full_name": "Jane Doe", "job_role_title": "CTO", "job_department": "Engineering", "linkedin_url": "https://linkedin.com/in/janedoe", "event_time": "2024-01-10"}],
        "strategic": [{"event_name": "new_partnership", "title": "AWS Partnership", "description": "Strategic co-sell agreement with AWS Marketplace.", "event_time": "2024-02-15"}],
        "enrichment": {"revenue_range": "$5M-$10M", "growth_rate": "45%", "market": "North America"},
    },
    "mock-biz-002": {
        "hiring": [
            {"event_name": "hiring_in_marketing_department", "job_titles": ["VP Marketing", "Demand Gen Manager"], "job_count": 4, "department": "Marketing"},
        ],
        "funding": [{"event_name": "new_funding_round", "funding_round": "Series C", "funding_amount": 50000000, "event_time": "2024-02-01", "investors": ["Tiger Global"]}],
        "leadership": [],
        "strategic": [{"event_name": "new_product", "title": "ShieldAI v3", "description": "Next-gen AI threat correlation engine launched.", "event_time": "2024-03-10"}],
        "enrichment": {"revenue_range": "$20M-$50M", "growth_rate": "60%", "market": "Global"},
    },
    "mock-biz-003": {
        "hiring": [{"event_name": "hiring_in_sales_department", "job_titles": ["Account Executive"], "job_count": 2, "department": "Sales"}],
        "funding": [{"event_name": "new_funding_round", "funding_round": "Series A", "funding_amount": 10000000, "event_time": "2023-05-20", "investors": ["Breakthrough Energy"]}],
        "leadership": [],
        "strategic": [],
        "enrichment": {"revenue_range": "$1M-$5M", "growth_rate": "30%", "market": "USA"},
    },
    "mock-biz-004": {
        "hiring": [{"event_name": "increase_in_engineering_department", "job_titles": ["Data Engineer", "ML Engineer"], "job_count": 6, "department": "Engineering"}],
        "funding": [{"event_name": "new_funding_round", "funding_round": "Series A", "funding_amount": 15000000, "event_time": "2024-01-15", "investors": ["Bessemer"]}],
        "leadership": [{"full_name": "Alex Kim", "job_role_title": "VP Product", "job_department": "Product", "linkedin_url": "", "event_time": "2024-02-01"}],
        "strategic": [{"event_name": "new_partnership", "title": "Snowflake Native App", "description": "Launched native app on Snowflake Marketplace.", "event_time": "2024-03-05"}],
        "enrichment": {"revenue_range": "$3M-$8M", "growth_rate": "50%", "market": "North America"},
    },
    "mock-biz-005": {
        "hiring": [{"event_name": "hiring_in_engineering_department", "job_titles": ["Platform Engineer", "SRE"], "job_count": 4, "department": "Engineering"}],
        "funding": [{"event_name": "new_funding_round", "funding_round": "Seed", "funding_amount": 5000000, "event_time": "2023-09-01", "investors": ["GV"]}],
        "leadership": [],
        "strategic": [],
        "enrichment": {"revenue_range": "$500K-$2M", "growth_rate": "80%", "market": "North America"},
    },
}

def _mock_match_business(name: str, website: str = None) -> Optional[str]:
    for c in _MOCK_COMPANIES:
        if c["name"].lower() == name.lower():
            log.info(f"[mock] match_business: '{name}' -> {c['explorium_id']}")
            return c["explorium_id"]
    fallback_id = f"mock-biz-{abs(hash(name)) % 9000 + 1000}"
    log.info(f"[mock] match_business: '{name}' not found, returning fallback {fallback_id}")
    return fallback_id

def _mock_search_companies(query_str: str = "", filters: dict = None) -> list[dict]:
    log.info(f"[mock] search_companies: query='{query_str}', filters={filters}, returning {len(_MOCK_COMPANIES)} companies")
    return list(_MOCK_COMPANIES)

def _mock_enrich_company(business_id: str) -> Optional[dict]:
    data = _MOCK_EVENTS.get(business_id, {}).get("enrichment")
    log.info(f"[mock] enrich_company: business_id={business_id} -> {data}")
    return data

def _mock_get_business_events(business_id: str, event_types: list[str]) -> list[dict]:
    biz = _MOCK_EVENTS.get(business_id, {})
    results = []
    if any("hiring" in et or "increase" in et for et in event_types):
        results.extend(biz.get("hiring", []))
    if any("funding" in et or "investment" in et or "ipo" in et for et in event_types):
        results.extend(biz.get("funding", []))
    if any("employee" in et for et in event_types):
        results.extend(biz.get("leadership", []))
    if any(et in ["merger_and_acquisitions", "new_product", "new_partnership", "cost_cutting"] for et in event_types):
        results.extend(biz.get("strategic", []))
    log.info(f"[mock] get_business_events: business_id={business_id}, types={event_types} -> {len(results)} events")
    return results

def _mock_fetch_prospects(business_id: str, job_levels: list = None, job_departments: list = None) -> list[dict]:
    log.info(f"[mock] fetch_prospects: b_id={business_id}")
    return [{
        "prospect_id": f"mock-prospect-{business_id}",
        "first_name": "Jane",
        "last_name": "Smith",
        "full_name": "Jane Smith",
        "job_title": "VP of Revenue",
        "job_level_main": "vp",
        "job_department_main": "sales",
        "linkedin": "linkedin.com/in/janesmith"
    }]

def _mock_enrich_contact(prospect_id: str) -> Optional[dict]:
    log.info(f"[mock] enrich_contact: prospect_id={prospect_id}")
    return {
        "professions_email": "jane.smith@example.com",
        "professional_email_status": "valid",
        "emails": [{"jsmith119@gmail.com": "personal"}],
        "mobile_phone": "+14155551234"
    }

def _mock_bulk_enrich_contacts(prospect_ids: list[str]) -> list[dict]:
    log.info(f"[mock] bulk_enrich_contacts: {len(prospect_ids)} IDs")
    return [
        {
            "prospect_id": pid,
            "data": {
                "professions_email": f"{pid}@example.com",
                "emails": [{"address": f"{pid}@example.com", "type": "professional"}]
            }
        }
        for pid in prospect_ids
    ]




# =============================================================================
# EXPORTED TOGGLE FUNCTIONS
# =============================================================================

def match_business(name: str, website: str = None) -> Optional[str]:
    if settings.USE_MOCK_DATA:
        return _mock_match_business(name, website)
    return _real_match_business(name, website)

def search_companies(query_str: str = "", filters: dict = None) -> list[dict]:
    if settings.USE_MOCK_DATA:
        return _mock_search_companies(query_str, filters)
    return _real_search_companies(query_str, filters)

def enrich_company(business_id: str) -> Optional[dict]:
    if settings.USE_MOCK_DATA:
        return _mock_enrich_company(business_id)
    return _real_enrich_company(business_id)

def fetch_prospects(business_id: str, job_levels: list = None, job_departments: list = None) -> list[dict]:
    if settings.USE_MOCK_DATA:
        return _mock_fetch_prospects(business_id, job_levels, job_departments)
    return _real_fetch_prospects(business_id, job_levels, job_departments)

def enrich_contact(prospect_id: str) -> Optional[dict]:
    if settings.USE_MOCK_DATA:
        return _mock_enrich_contact(prospect_id)
    return _real_enrich_contact(prospect_id)

def bulk_enrich_contacts(prospect_ids: list[str]) -> list[dict]:
    if settings.USE_MOCK_DATA:
        return _mock_bulk_enrich_contacts(prospect_ids)
    return _real_bulk_enrich_contacts(prospect_ids)

def get_business_events(business_id: str, event_types: list[str]) -> list[dict]:
    if settings.USE_MOCK_DATA:
        return _mock_get_business_events(business_id, event_types)
    return _real_get_business_events(business_id, event_types)