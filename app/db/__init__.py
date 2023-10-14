import asyncio

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from app.config import config
from app.models import Base


engine = create_async_engine(config.db.url, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        await db.close()


async def migrate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
        await conn.close()
    async for _ in get_db():
        pass


def migrate_sync():
    asyncio.run(migrate())
