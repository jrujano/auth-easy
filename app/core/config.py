# from pydantic import BaseSettings
import os
from pydantic_settings import BaseSettings  # NEW


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Auth-Easy"
    # DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./velardiapp.db")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./auth-easy.db")


settings = Settings()
