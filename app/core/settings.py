from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database
    db_engine: str
    db_driver: str | None = None
    db_user: str  | None = None
    db_password: str | None = None
    db_host: str | None = None
    db_port: int | None = None
    db_name: str | None = None

    model_config = SettingsConfigDict(env_file=".env")
