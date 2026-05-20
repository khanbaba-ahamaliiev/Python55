from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8080
    MAX_FILMS: int | None = None
    data_file_path: str = "./films.json"

    model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8"
    )

settings = Settings()
