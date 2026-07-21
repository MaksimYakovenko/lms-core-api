from __future__ import annotations

# Module to interface with MCP tools as the source of data truth.
import os
import asyncpg
from typing import Any, Awaitable, Callable

class MCPDataValidator:
    """
    A class responsible for validating and ensuring consistency of data retrieved from MCP tools.
    """

    def __init__(self, db_url: str):
        """
        Initialize the MCPDataValidator.

        Args:
            db_url (str): Database URL for connecting to the main PostgreSQL database.
        """
        self.db_url = db_url

    async def fetch_data(self, key: str) -> dict[str, Any]:
        """
        Retrieve and validate data from the MCP tools.

        Args:
            key (str): The key identifying the data to retrieve.

        Returns:
            dict[str, Any]: The validated data.
        """
        async with asyncpg.create_pool(self.db_url) as pool:
            async with pool.acquire() as connection:
                query = "SELECT * FROM mcp_data WHERE key = $1"
                result = await connection.fetchrow(query, key)
                if result is None:
                    raise ValueError(f"No data found for key: {key}")
                return dict(result)
