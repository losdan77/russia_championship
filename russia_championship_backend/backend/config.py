from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str 
    
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str

    SECRET_WORD: str
    HASH_ALGORITHM: str

    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASS: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_SECRET_KEY: str
    GOOGLE_REDIRECT_URI_BACK: str
    GOOGLE_REDIRECT_URI_FRON: str
    GOOGLE_TOKEN_URI: str

    @property
    def google_redirect_url(self):
        return f'https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI_BACK}&scope=openid%20profile%20email&access_type=offline'

    YANDEX_CLIENT_ID: str
    YANDEX_SECRET_KEY: str
    YANDEX_REDIRECT_URI: str
    YANDEX_TOKEN_URI: str

    @property
    def yandex_redirect_url(self):
        return f'https://oauth.yandex.ru/authorize?response_type=code&client_id={self.YANDEX_CLIENT_ID}&redirect_uri={self.YANDEX_REDIRECT_URI}'
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()