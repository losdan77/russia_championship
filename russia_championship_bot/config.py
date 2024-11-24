from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    TOKEN: str
    ADMIN_ID: str
    
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASS: str

    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()