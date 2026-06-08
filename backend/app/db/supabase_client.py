from supabase import create_client, Client
from app.core.config import Settings

_client: Client | None = None

def get_supabase_client() -> Client:
    global _client
    if _client is None:
        settings = Settings()
        _client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)
    return _client