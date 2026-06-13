from typing import AsyncGenerator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    AsyncSession
)


class Database:
    def __init__(
        self, 
        db_engine: str, 
        db_driver: str | None = None,
        db_user: str  | None = None,
        db_password: str | None = None,
        db_host: str | None = None,
        db_port: int | None = None,
        db_name: str | None = None,
    ):
        if db_driver:
            db_url=f"{db_engine}+{db_driver}"
        else:
            db_url=db_engine

        db_url = URL.create(
            drivername=db_url,
            username=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name,
        )

        self._engine = create_async_engine(db_url, echo=True)

        self._session_factory = async_sessionmaker(bind=self._engine, expire_on_commit=False)
    

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_factory() as session:
            yield session

    async def close(self):
        await self._engine.dispose()