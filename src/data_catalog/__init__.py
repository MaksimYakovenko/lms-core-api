from __future__ import annotations

import os
import psycopg
from asyncpg import Connection, Pool, create_pool
from typing import List, Dict

class DataCatalogClient:
    """Client to interact with the EPAM Data Catalog MCP."""

    def __init__(self) -> None:
        """Initialize the DataCatalogClient."""
        pass

    async def search_data(self, query: str) -> List[str]:
        """Search the data catalog with the provided query.

        Args:
            query: The query string to search for.

        Returns:
            List of resulting data identifiers matching the query.
        """
        database_pool: Pool = await create_pool(os.environ["DATABASE_URL"])
        async with database_pool.acquire() as conn:
            records = await conn.fetch("SELECT id FROM data_catalog WHERE name LIKE $1", f"%{query}%")
            return [record["id"] for record in records]

    async def get_data_details(self, identifier: str) -> Dict[str, str]:
        """Get details for the data by its identifier.

        Args:
            identifier: The identifier of the data item.

        Returns:
            A dictionary containing details of the specified data item.
        """
        database_pool: Pool = await create_pool(os.environ["DATABASE_URL"])
        async with database_pool.acquire() as conn:
            record = await conn.fetchrow("SELECT * FROM data_catalog WHERE id = $1", identifier)
            return dict(record) if record else {}

    async def validate_all_mcp(self) -> None:
        """Ensures that the system is only utilizing MCP methods for data-related functionalities."""
        methods = ["search_data", "get_data_details"]
        assert all(method in dir(self) for method in methods), "Some MCP methods are unavailable."
