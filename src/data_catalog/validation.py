from __future__ import annotations

import os
from asyncpg.pool import Pool, create_pool
from typing import Any

class DataValidator:
    """A class to validate data operations against requirements."""

    def __init__(self, db_url: str) -> None:
        """Initialize with the database connection string."""
        self._db_url = db_url
        self._pool: Pool | None = None

    async def setup(self) -> None:
        """Set up the database connection pool."""
        if self._pool is None:
            self._pool = await create_pool(dsn=self._db_url)

    async def validate_data_source(self, source_id: int) -> bool:
        """Validate that the source exclusively uses MCP for queries."""
        assert self._pool is not None, "The pool must be initialized with setup."
        async with self._pool.acquire() as connection:
            query = (
                "SELECT is_mcp_source FROM source_table WHERE id = $1"
            )
            result = await connection.fetchval(query, source_id)
            return bool(result)

    async def teardown(self) -> None:
        """Teardown the database connection pool."""
        if self._pool is not None:
            await self._pool.close()
            self._pool = None
