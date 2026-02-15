from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

DATABASE_URL = (f"postgresql+asyncpg://{settings.DB_USER}"
                f":{settings.DB_PASSWORD}@{settings.DB_HOST}:"
                f"{settings.DB_PORT}/"
                f"{settings.DB_NAME}")

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
