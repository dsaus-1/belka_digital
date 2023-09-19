from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

SECRET = os.environ.get('SECRET')
SECRET_MANAGER = os.environ.get('SECRET_MANAGER')

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")