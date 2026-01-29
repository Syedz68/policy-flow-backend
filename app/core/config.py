from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")
    ENV: str = Field(..., env="ENV")
    DEBUG: bool = Field(..., env="DEBUG")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field(..., env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_MINUTES: int = Field(..., env="REFRESH_TOKEN_EXPIRE_MINUTES")
    ACCESS_TOKEN_EXPIRE_DAYS: int = Field(..., env="ACCESS_TOKEN_EXPIRE_DAYS")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(..., env="REFRESH_TOKEN_EXPIRE_DAYS")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    ALLOWED_ORIGINS: list[str] = Field(..., env="ALLOWED_ORIGINS")
    USE_DEFAULT_OTP: bool = Field(..., env="USE_DEFAULT_OTP")
    DEFAULT_OTP_VALUE: str = Field(..., env="DEFAULT_OTP_VALUE")
    OTP_EXPIRY_MINUTES: int = Field(..., env="OTP_EXPIRY_MINUTES")
    OTP_MAX_ATTEMPTS: int = Field(..., env="OTP_MAX_ATTEMPTS")
    OTP_RATE_LIMIT_SECONDS: int = Field(..., env="OTP_RATE_LIMIT_SECONDS")

    class Config:
        env_file = ".env.example"
        env_file_encoding = "utf-8"

settings = Settings()