from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:admin@192.168.1.128:5433/sample_db"

settings = Settings() 