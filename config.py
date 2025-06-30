from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    # secret_key: str  # Aprovechamos de agregar la SECRET_KEY que usaremos después
    access_token_expire_minutes: int = 30 # Y el tiempo de expiración

    class Config:
        env_file = ".env"

settings = Settings()