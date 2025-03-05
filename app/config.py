from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "My App"
    host: str
    port: int
    reload: bool
    database_url: str
    redis_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()