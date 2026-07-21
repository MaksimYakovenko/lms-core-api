from __future__ import annotations

import os
from asyncpg.pool import Pool, create_pool

class DataValidatorMCP:  # Changed the class name for differentiation
    """
    A class to validate that the system exclusively uses MCP as the data source.
    """

    def __init__(self, db_url: str) -> None:
        """
        Initialize a new instance of DataValidatorMCP.

        Args:
            db_url: The database connection URL.
        """
        self._db_url = db_url
        self._pool: Pool | None = None

    async def setup(self) -> None:
        """
        Asynchronously setup the database connection pool.
        """
        if self._pool is None:
            self._pool = await create_pool(dsn=self._db_url)

    async def validate_exclusive_use_of_mcp(self) -> bool:
        """
        Validate that the implemented system exclusively uses MCP as the data source.

        Returns:
            bool: True if exclusively using MCP, False otherwise.
        """
        assert self._pool is not None, "Database connection pool is not initialized."

        query = "SELECT EXCLUSIVE_USE_OF_MCP FROM SYSTEM_VALIDATION WHERE SYSTEM_ID = 1"
        async with self._pool.acquire() as connection:
            result = await connection.fetchval(query)

        return bool(result)

    async def teardown(self) -> None:
        """
        Asynchronously close the database connection pool.
        """
        if self._pool is not None:
            await self._pool.close()
            self._pool = None
