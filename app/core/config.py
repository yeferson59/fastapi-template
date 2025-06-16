from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Project"
    debug: bool = False
    api_prefix: str = "/api"
    api_version: str = "v1"
    allowed_hosts: list[str] = ["*"]
    database_url: str = "sqlite:///test.sqlite3"
    secret_key: str = "your-secret-key"
    port: int = 8000
    environment: str = "development"
    turso_auth_token: str = "your-auth-token"
    is_turso: bool = False
    pythonpath: str = "."

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.*"), env_file_encoding="utf-8", extra="allow"
    )


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def get_full_api_prefix() -> str:
    settings = get_settings()
    return f"{settings.api_prefix}/{settings.api_version}"
