from app.core.database import Database
from app.core.settings import Settings
from functools import lru_cache


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def _get_database():
    settings = get_settings()

    return Database(
        db_engine=settings.db_engine,
        db_user=settings.db_user,
        db_password=settings.db_password,
        db_host=settings.db_host,
        db_port=settings.db_port,
        db_name=settings.db_name
    )


def db_session():
    db = _get_database()
    return db.get_session