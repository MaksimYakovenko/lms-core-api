from __future__ import annotations

import os
from collections.abc import Awaitable

from asyncpg import create_pool, Pool

DATABASE_URL = os.getenv("DATABASE_URL")

class DataCatalog:
    """Interacts with the Data Catalog for metadata search."""

    def __init__(self, db_url: str) -> None:
        if not db_url:
            raise ValueError("Database URL must be provided.")
        self.db_url = db_url
        self._db_pool: Pool | None = None

    async def initialize(self) -> None:
        self._db_pool = await create_pool(dsn=self.db_url)

    async def close(self) -> None:
        if self._db_pool is not None:
            await self._db_pool.close()
            self._db_pool = None

    async def search_data(self, query: str, parameters: tuple = ()) -> list[dict]:
        if self._db_pool is None:
            raise RuntimeError("DataCatalog has not been initialized.")

        async with self._db_pool.acquire() as connection:
            rows = await connection.fetch(query, *parameters)
            return [dict(row) for row in rows]

    async def __aenter__(self) -> DataCatalog:
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

def build_query() -> str:
    """Prepares the query to fetch Kafka topic entities."""
    return "SELECT * FROM public.entities WHERE topic_name=$1 LIMIT 1;"

async def query_kafka_topic(topic_name: str) -> dict | None:
    """Queries the Data Catalog for a Kafka topic entity."""
    if not topic_name:
        raise ValueError("Topic name cannot be empty.")

    async with DataCatalog(DATABASE_URL) as catalog:
        query = build_query()
        results = await catalog.search_data(query, (topic_name,))
        return results[0] if results else None
