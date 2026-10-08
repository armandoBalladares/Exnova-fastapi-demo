from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    EXNOVA_EMAIL: str = ""
    EXNOVA_PASSWORD: str = ""
    EXNOVA_MODE: str = "demo"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
