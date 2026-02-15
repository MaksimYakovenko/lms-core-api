import asyncio
from db.database import engine, Base
from models import news_model, auth_model


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_and_create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
