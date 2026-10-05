from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from collections.abc import AsyncGenerator

CONN_STR = "postgresql+asyncpg://jconnix@localhost/cmdb"

engine = create_async_engine(CONN_STR, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]: # -> define the return type
    async with async_session() as session: # init and return a session
        yield session
