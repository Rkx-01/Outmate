import os
from pydantic_settings import BaseSettings
from typing import Optional

# LinkedIn Categories - From Explorium official docs
# https://developers.explorium.ai/categories
VALID_LINKEDIN_CATEGORIES = [
    # Software & Tech
    "software development",
    "computer hardware",
    "computer networking",
    "information technology & services",
    "it services and it consulting",
    "data infrastructure and analytics",
    "data security software products",
    "desktop computing software products",
    "mobile computing software products",
    "embedded software products",
    "cloud computing",
    # Finance & Banking
    "financial services",
    "banking",
    "investment banking",
    "capital markets",
    "insurance",
    "venture capital and private equity principals",
    # Security & Risk
    "computer and network security",
    "cybersecurity",
    "security and investigations",
    "security systems services",
    # Healthcare
    "hospital & health care",
    "biotechnology",
    "pharmaceutical manufacturing",
    "medical device",
    # Telecommunications
    "telecommunications",
    "telecommunications carriers",
    "wireless services",
    # Manufacturing & Hardware
    "semiconductors",
    "semiconductor manufacturing",
    "computer hardware manufacturing",
    # Analytics & Research
    "market research",
    "research services",
    "business intelligence platforms",
    # Internet & Digital
    "internet",
    "internet marketplace platforms",
    "social networking platforms",
    "online media",
]

class Settings(BaseSettings):

    GOOGLE_API_KEY: str = "dummy"
    GOOGLE_API_KEYS: Optional[str] = None  # Comma-separated list
    DATABASE_URL: str = "sqlite:///./data/gtm_intelligence.db"
    MEMPALACE_PATH: str = "./mempalace_data"
    GTM_API_KEY: str = "dev-key"
    USE_MOCK_DATA: bool = True
    EXPLORIUM_API_KEY: Optional[str] = None
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    class Config:
        env_file = ".env"

settings = Settings()
