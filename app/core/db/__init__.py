import asyncio

from loguru import logger
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import config
from app.models import Base

engine = create_async_engine(config.db.url, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        await db.close()


async def migrate(drop_all: bool = False):
    logger.info("🚀 Migrating database")
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


def migrate_sync(drop_all: bool = False):
    asyncio.run(migrate(drop_all))
