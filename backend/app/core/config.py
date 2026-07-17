from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from logging import INFO, DEBUG, WARNING, ERROR, CRITICAL

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    OPENAI_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_SERVICE_ROLE_KEY: str
    COHERE_API_KEY: str

    # Optional settings
    LOG_LEVEL: int = INFO
    CHAT_MODEL: str = "gpt-4o"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    RERANKING_MODEL: str = "rerank-v4.0-fast"
    DOCUMENTS_PATH: str = "documents"
    RETRIEVAL_TOP_K: int = 15
    RERANKING_TOP_K: int = 5
    MIN_VECTOR_SIMILARITY_SCORE: float = 0.20
    MIN_RERANKING_SCORE: float = 0.45

@lru_cache(maxsize=1)
def get_config() -> Settings:
    return Settings()