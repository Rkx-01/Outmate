import os, logging
from typing import Optional, Dict, List, Union

log = logging.getLogger(__name__)

# =============================================================================
# THEIRSTACK API — COMMENTED OUT (mocked below)
# Original code preserved; re-enable by uncommenting and removing mock section.
# =============================================================================

# import httpx, functools, time
# THEIRSTACK_BASE = "https://api.theirstack.com/v1"
# HEADERS = lambda: {"Authorization": f"Bearer {os.getenv('THEIRSTACK_API_KEY')}"}
#
# def with_retry(max_retries=2, backoff=1.0):
#     def decorator(fn):
#         @functools.wraps(fn)
#         def wrapper(*args, **kwargs):
#             for attempt in range(max_retries + 1):
#                 try:
#                     return fn(*args, **kwargs)
#                 except httpx.HTTPStatusError as e:
#                     if e.response.status_code == 429:
#                         time.sleep(backoff * (attempt + 1))
#                         continue
#                     if e.response.status_code in (401, 403):
#                         raise ValueError(f"API auth failed: {fn.__name__} — check .env")
#                     return None
#                 except (httpx.TimeoutException, httpx.RequestError):
#                     return None
#             return None
#         return wrapper
#     return decorator
#
# @with_retry()
# def get_tech_stack(company_name: str) -> list[str]:
#     response = httpx.get(
#         f"{THEIRSTACK_BASE}/companies/search",
#         params={"name": company_name, "include_technologies": True},
#         headers=HEADERS(), timeout=15.0
#     )
#     response.raise_for_status()
#     companies = response.json().get("data", [])
#     if not companies:
#         return []
#     return [t.get("name") for t in companies[0].get("technologies", []) if t.get("name")]
#
# @with_retry()
# def get_hiring_signals(company_name: str) -> list[str]:
#     response = httpx.post(
#         f"{THEIRSTACK_BASE}/jobs/search",
#         json={
#             "company_name_or": [company_name],
#             "job_title_or": [
#                 "VP Sales", "Chief Revenue Officer", "CRO", "Head of Revenue",
#                 "Head of Sales", "Sales Director", "SDR Manager",
#                 "Account Executive", "Revenue Operations", "VP Marketing"
#             ],
#             "limit": 20,
#             "order_by": [{"desc": True, "field": "discovered_at"}]
#         },
#         headers=HEADERS(), timeout=15.0
#     )
#     response.raise_for_status()
#     return [job.get("job_title") for job in response.json().get("data", []) if job.get("job_title")]
#
# @with_retry()
# def get_funding_info(company_name: str) -> Optional[dict]:
#     response = httpx.get(
#         f"{THEIRSTACK_BASE}/companies/search",
#         params={"name": company_name, "include_funding": True},
#         headers=HEADERS(), timeout=15.0
#     )
#     response.raise_for_status()
#     companies = response.json().get("data", [])
#     if not companies:
#         return None
#     c = companies[0]
#     return {
#         "funding_amount": c.get("last_funding_amount_usd"),
#         "funding_round": c.get("last_funding_round"),
#         "funding_date": c.get("last_funding_date"),
#         "investors": c.get("investors", [])
#     }


# =============================================================================
# MOCK IMPLEMENTATIONS
# Mirrors the exact signatures of the TheirStack API functions above.
# =============================================================================

_MOCK_TECH_STACKS = {
    "TechFlow AI":  ["React", "Python", "FastAPI", "AWS", "PostgreSQL", "Redis", "Terraform"],
    "CyberShield":  ["Rust", "Python", "Kubernetes", "Snowflake", "Kafka", "GCP"],
    "GreenGrid":    ["Vue.js", "Go", "GCP", "MongoDB", "TimescaleDB"],
    "DataPulse":    ["dbt", "Airflow", "Snowflake", "Python", "Kubernetes", "AWS"],
    "ScaleOps":     ["Go", "Kubernetes", "Prometheus", "Grafana", "AWS", "Helm"],
}

_MOCK_HIRING_SIGNALS = {
    "TechFlow AI":  ["VP Sales", "Senior Account Executive", "Enterprise Account Executive"],
    "CyberShield":  ["VP Marketing", "Demand Gen Manager"],
    "GreenGrid":    ["Account Executive"],
    "DataPulse":    ["Revenue Operations Manager", "Head of Sales"],
    "ScaleOps":     [],
}


def get_tech_stack(company_name: str) -> list[str]:
    """Mock: Return technology stack for a company."""
    stack = _MOCK_TECH_STACKS.get(company_name, ["JavaScript", "Python", "AWS"])
    log.info(f"[mock] get_tech_stack: company='{company_name}' -> {stack}")
    return stack


def get_hiring_signals(company_name: str) -> list[str]:
    """Mock: Return active GTM-relevant job openings for a company."""
    signals = _MOCK_HIRING_SIGNALS.get(company_name, [])
    log.info(f"[mock] get_hiring_signals (theirstack): company='{company_name}' -> {signals}")
    return signals


def get_funding_info(company_name: str) -> Optional[dict]:
    """Mock: Return latest funding data for a company."""
    # TheirStack funding is redundant with Explorium in this mock; return None to avoid duplication
    log.info(f"[mock] get_funding_info (theirstack): company='{company_name}' -> None (deferred to Explorium)")
    return None