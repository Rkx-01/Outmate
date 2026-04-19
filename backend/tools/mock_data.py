import random

COMPANIES_DB = [
    {
        "name": "TechFlow AI",
        "industry": "Software",
        "location": "San Francisco, CA",
        "description": "Workflow automation for engineering teams.",
        "website": "https://techflow.ai",
        "funding_round": "Series B",
        "funding_amount": 25000000,
        "funding_date": "2023-11-15",
        "employee_count": 120,
        "tech_stack": ["React", "Python", "AWS", "PostgreSQL", "Redis"],
        "hiring_signals": ["Hiring VP Sales", "Hiring Senior Backend Engineer"],
        "leadership_changes": [{"name": "Jane Doe", "role": "CTO", "date": "2024-01-10"}]
    },
    {
        "name": "BadData Inc",
        "industry": "",
        "location": "Nowhere",
        "description": "This company will trigger the critic.",
        "website": None,
        "funding_round": "Seed",
        "funding_amount": 100000,
        "funding_date": "2020-01-01",
        "employee_count": -1,
        "tech_stack": [],
        "hiring_signals": [],
        "leadership_changes": []
    }
]

def inject_noise(data: dict) -> dict:
    if data.get("name") == "BadData Inc":
        return data # Keep it bad
    
    noisy_data = data.copy()
    # 30% missing fields
    for key in list(noisy_data.keys()):
        if random.random() < 0.3:
            noisy_data[key] = None
    
    # 20% stale/bad data
    if random.random() < 0.2:
        if "funding_amount" in noisy_data and noisy_data["funding_amount"] is not None:
             noisy_data["funding_amount"] = noisy_data["funding_amount"] * 0.1
        if "employee_count" in noisy_data and noisy_data["employee_count"] is not None:
             noisy_data["employee_count"] = -1
             
    return noisy_data

COMPANIES_DB.extend([
    {
        "name": "GreenGrid",
        "industry": "CleanTech",
        "location": "Austin, TX",
        "description": "Smart grid management software.",
        "website": "https://greengrid.io",
        "funding_round": "Series A",
        "funding_amount": 10000000,
        "funding_date": "2022-05-20",
        "employee_count": 45,
        "tech_stack": ["Vue.js", "Go", "GCP", "MongoDB"],
        "hiring_signals": ["Hiring Account Executive"],
        "leadership_changes": []
    },
    {
        "name": "CyberShield",
        "industry": "Cybersecurity",
        "location": "Boston, MA",
        "description": "AI-powered threat detection.",
        "website": "https://cybershield.net",
        "funding_round": "Series C",
        "funding_amount": 50000000,
        "funding_date": "2024-02-01",
        "employee_count": 250,
        "tech_stack": ["Rust", "Python", "Kubernetes", "Snowflake"],
        "hiring_signals": ["Hiring Security Researcher", "Hiring VP Marketing"],
        "leadership_changes": []
    }
])
