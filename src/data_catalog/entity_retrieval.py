from __future__ import annotations

from typing import Any
import os
import asyncpg

class DataCatalog:
    """Class for interacting with the Data Catalog."""

    def __init__(self, db_url: str) -> None:
        """Initialize with the database URL from environment variable."""
        self.db_url = db_url

    async def _get_db_pool(self):
        """Returns a connection pool for the database."""
        return await asyncpg.create_pool(dsn=self.db_url)

    async def retrieve_entity_details(
        self, entity_id: str
    ) -> dict[str, Any]:
        """Retrieve details for the given entity ID."""
        async with await self._get_db_pool() as pool:
            async with pool.acquire() as connection:
                query = (
                    "SELECT entity_id, basic, governance, links "
                    "FROM entities "
                    "WHERE entity_id = $1"
                )
                result = await connection.fetchrow(query, entity_id)
                if result is None:
                    raise ValueError(f"Entity {entity_id} not found.")
                return {
                    "entity_id": result["entity_id"],
                    "basic": result["basic"],
                    "governance": result["governance"],
                    "links": result["links"],
                }

def get_environment_variable(name: str) -> str:
    if name not in os.environ:
        raise EnvironmentError(f"Environment variable {name} is not set.")
    return os.environ[name]

def create_data_catalog() -> DataCatalog:
    db_url = get_environment_variable("DATABASE_URL")
    return DataCatalog(db_url=db_url)
