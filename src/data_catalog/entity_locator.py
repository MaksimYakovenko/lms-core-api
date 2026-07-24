from __future__ import annotations

from typing import Sequence
import asyncio
from asyncpg import Connection, create_pool
import os

async def locate_entities(filter_conditions: dict[str, str]) -> Sequence[dict[str, str]]:
    """Retrieve entities matching the provided filter conditions."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise EnvironmentError("DATABASE_URL environment variable not set.")
    
    query = "SELECT * FROM entities WHERE " + " AND ".join([f"{key} = ${idx}" for idx, key in enumerate(filter_conditions, start=1)])

    pool = await create_pool(dsn=database_url)
    async with pool.acquire() as connection:
        results = await connection.fetch(query, *filter_conditions.values())
        return [dict(record) for record in results]
