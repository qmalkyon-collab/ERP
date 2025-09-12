from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    APP_NAME: str = "ERP-MVP"
    APP_SECRET: str = "change_me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    ADMIN_EMAIL: str = "admin@example.com"
    ADMIN_PASSWORD: str = "ChangeMe123!"
    ADMIN_TENANT: str = "default"

    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@db:5432/erp"

settings = Settings()