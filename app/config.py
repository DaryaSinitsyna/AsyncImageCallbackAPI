from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str

    PAT: str
    USER_ID: str
    APP_ID: str

    MODEL_ID: str
    MODEL_VERSION_ID: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
