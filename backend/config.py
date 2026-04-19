import os
from pydantic_settings import BaseSettings
from typing import Optional

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
