from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_TITLE: str = "FastAPI Weather API Service"
    PROJECT_VERSION: str = "1.0.0"

    OPEN_WEATHER_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
