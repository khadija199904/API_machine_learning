from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Cardio Risk API"

    class Config:
        env_file = ".env"

settings = Settings()
