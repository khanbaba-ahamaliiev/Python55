from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_text: str = 'hello'
    password: str | None = None

    min_num: int = 10
    max_num: int = 100

    # чтение настроек из .env

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

# создать обьект класса
settings = Settings()

print(settings.password)
