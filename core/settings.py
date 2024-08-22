import os
import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    # server related
    ENV: str
    APP_HOST: str = "localhost"
    APP_PORT: int = 8080

    # database related
    DB_URL: str
    DB_PORT: int
    DB_NAME: str
    DB_PWD: str
    DB_USR: str

    # JWT Token related
    SECRET_KEY: str
    REFRESH_SECRET_KEY: str
    ALGORITHM: str
    TIMEOUT: int
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=DOTENV)


class DevelopmentConfig(Settings):
    DEBUG: bool = True


class ProductionConfig(Settings):
    DEBUG: bool = False


def get_settings():
    dotenv.load_dotenv(dotenv_path=DOTENV)
    env = os.getenv("ENV")
    config_type = {
        "development": DevelopmentConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


settings = get_settings()
