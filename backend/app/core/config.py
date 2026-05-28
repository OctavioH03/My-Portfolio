from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from logging import INFO, DEBUG, WARNING, ERROR, CRITICAL

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    openai_api_key: str
    supabase_url: str
    supabase_service_role_key: str

    # Optional settings
    log_level: int = INFO
    chat_model: str = "gpt-4o"
    embedding_model: str = "text-embedding-3-small"
    documents_path: str = "documents"

@lru_cache(maxsize=1)
def get_config() -> Settings:
    return Settings()