import asyncio

from loguru import logger
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from ..config import config
from ...models import Base


def get_session():
    engine = create_async_engine(config.db.url, echo=True)
    Session = async_sessionmaker(engine, expire_on_commit=False)
    return engine, Session


async def get_db():
    engine, Session = get_session()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db = Session()
    try:
        yield db
    finally:
        await db.close()


async def migrate(drop_all: bool = False):
    logger.info("🚀 Migrating database")
    engine, _ = get_session()
    async with engine.begin() as conn:
        if drop_all:
            logger.warning("⚠️  Dropping all tables")
            await conn.run_sync(Base.metadata.drop_all)
        logger.info("👷 Creating all tables")
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
        await conn.close()
        logger.info("🏁 Database migrated")
    async for _ in get_db():
        pass


async def drop_all():
    engine, _ = get_session()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.commit()
        await conn.close()


def migrate_sync(drop_all: bool = False):
    asyncio.run(migrate(drop_all))


def drop_all_sync():
    asyncio.run(drop_all())
