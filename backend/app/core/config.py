from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings, loaded from environment variables / .env file.
    Add new config values here as the project grows.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Xthings Attendance API"
    app_env: str = "development"
    debug: bool = True

    database_url: str = (
        "postgresql+psycopg://xthings:xthings_dev_password@localhost:5432/xthings_db"
    )

    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
