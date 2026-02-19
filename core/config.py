import os
from dotenv import load_dotenv

load_dotenv()


class Setting:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', 5432)
    DB_NAME = os.getenv('DB_NAME', 'news')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv(
        'ACCESS_TOKEN_EXPIRE_MINUTES', 15))
    REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv(
        'REFRESH_TOKEN_EXPIRE_DAYS', 7))
    ALGORITHM = os.getenv('ALGORITHM', 'HS256')

settings = Setting()
