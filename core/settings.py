from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    
    class Config:
        env_file = ".env"


env = Settings()

POSTGRES_DB = env.POSTGRES_DB
POSTGRES_USER = env.POSTGRES_USER
POSTGRES_PASSWORD = env.POSTGRES_PASSWORD
POSTGRES_HOST = env.POSTGRES_HOST
POSTGRES_PORT = env.POSTGRES_PORT
