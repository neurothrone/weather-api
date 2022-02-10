from pydantic import BaseSettings


class Settings(BaseSettings):
    OPEN_WEATHER_API_KEY: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
