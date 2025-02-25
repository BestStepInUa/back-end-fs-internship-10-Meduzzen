from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "My App"
    data_file: str
    host: str
    port: int
    reload: bool

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()