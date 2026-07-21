from __future__ import annotations

import os
from collections.abc import Awaitable

from asyncpg.pool import create_pool

DATABASE_URL = os.getenv("DATABASE_URL")

class DataCatalog:
    """Interacts with the Data Catalog for metadata search."""

    def __init__(self) -> None:
        if not DATABASE_URL:
            raise EnvironmentError("Environment variable DATABASE_URL not set.")

        self.db_pool = create_pool(dsn=DATABASE_URL)

    async def search_data(self, query: str) -> list[dict]:
        async with self.db_pool.acquire() as connection:
            rows = await connection.fetch(query)
            return [dict(row) for row in rows]

def query_kafka_topic(topic_name: str) -> dict | None:
    """Queries the Data Catalog for a Kafka topic entity."""
    catalog = DataCatalog()
    query = f"SELECT * FROM public.entities WHERE topic_name='{topic_name}' LIMIT 1;"
    results = await catalog.search_data(query)
    return results[0] if results else None
