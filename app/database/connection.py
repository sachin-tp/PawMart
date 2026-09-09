import psycopg

from app.config.settings import settings


def get_db_connection():
    return psycopg.connect(settings.DATABASE_URL)