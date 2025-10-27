from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Cardio Risk API"
    DATABASE_URL: str = "sqlite:///./cardio.db"

    class Config:
        env_file = ".env"

settings = Settings()
