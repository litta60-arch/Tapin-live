# Configuration helpers (expand as needed)
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@postgres:5432/tapin"
    redis_url: str = "redis://redis:6379/0"
    livekit_api_key: str | None = None
    livekit_api_secret: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
