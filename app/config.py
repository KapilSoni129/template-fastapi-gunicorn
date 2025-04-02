from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings. ADD envs"""
    OPENAI_API_KEY: str
    MODEL_NAME: str
    TEMPERATURE: float
    MAX_TOKENS: int

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()