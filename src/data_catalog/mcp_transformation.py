from __future__ import annotations

import os
import asyncpg
import logging

class MCPInteractor:
    """Interface for managing interactions with the MCP data source."""

    def __init__(self, connection_url: str) -> None:
        self.connection_url = connection_url

    async def fetch_data(self, query: str) -> list[dict[str, object]]:
        """Fetch data from MCP using the provided query."""
        try:
            async with asyncpg.create_pool(self.connection_url) as pool:
                async with pool.acquire() as connection:
                    rows = await connection.fetch(query)
                    return [dict(row) for row in rows]
        except Exception as exc:
            logging.error("Error fetching data from MCP: %s", str(exc))
            return []

class DataCatalog:
    """Data catalog operations relying exclusively on MCP."""

    def __init__(self, mcp_interactor: MCPInteractor) -> None:
        self.mcp_interactor = mcp_interactor

    async def transform_data(self, query: str) -> list[dict[str, object]]:
        """Execute transformation fetching data via MCP."""
        return await self.mcp_interactor.fetch_data(query)

# Configuration
MCP_CONNECTION_URL = os.environ.get("DATABASE_URL", "")
mcp_interactor = MCPInteractor(connection_url=MCP_CONNECTION_URL)
data_catalog = DataCatalog(mcp_interactor=mcp_interactor)
