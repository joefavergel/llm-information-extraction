from functools import lru_cache
from typing import Any, Dict, Optional

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings for the package
    """
    OPENAI_API_KEY: Optional[SecretStr] = Field(..., env="OPENAI_API_KEY")
    GEMINI_API_KEY: Optional[SecretStr] = Field(..., env="GEMINI_API_KEY")

@lru_cache()
def get_settings() -> BaseSettings:
    """Get the settings for the package"""
    return Settings()


settings: Settings = Settings()
