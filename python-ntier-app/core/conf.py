from functools import lru_cache
from typing import Literal,Dict
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BasePath = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    """Global Settings"""
    model_config = SettingsConfigDict(env_file=f'{BasePath}/.env', env_file_encoding='utf-8', extra='ignore')

    # Env Config
    ENVIRONMENT: Literal['dev', 'pro']

    #Env SQLITE
    SQLITE_DB_NAME: str

    # FastAPI
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'FastAPI'
    VERSION: str = '1.0.0'
    DESCRIPTION: str = 'Python N Tier Example'
    DOCS_URL: str = f'{API_V1_STR}/docs'
    REDOCS_URL: str = f'{API_V1_STR}/redocs'
    OPENAPI_URL: str = f'{API_V1_STR}/openapi'

    @model_validator(mode='before')
    @classmethod
    def validate_openapi_url(cls, values):
        if values['ENVIRONMENT'] == 'pro':
            values['OPENAPI_URL'] = None
        return values

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # Middleware
    MIDDLEWARE_CORS: bool = True

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()

