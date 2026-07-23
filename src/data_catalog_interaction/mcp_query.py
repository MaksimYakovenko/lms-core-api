from __future__ import annotations

import os
import json
from collections.abc import Callable
from typing import Any
from psycopg.errors import DatabaseError
from asyncpg import create_pool

class MCPDataHandler:
    def __init__(self) -> None:
        self.database_url = os.getenv('DATABASE_URL')
        if self.database_url is None:
            raise ValueError("DATABASE_URL environment variable is not set")

    async def search_data(self, query: str) -> list[str]:
        async with create_pool(self.database_url) as pool:
            try:
                async with pool.acquire() as connection:
                    rows = await connection.fetch("SELECT resource_name FROM mcp_data WHERE query = $1", query)
                    return [row['resource_name'] for row in rows]
            except DatabaseError as err:
                raise RuntimeError("Database error occurred during search_data") from err

    async def get_data_details(self, resource_name: str) -> dict[str, Any]:
        async with create_pool(self.database_url) as pool:
            try:
                async with pool.acquire() as connection:
                    rows = await connection.fetch("SELECT * FROM mcp_data WHERE resource_name = $1", resource_name)
                    if rows:
                        return dict(rows[0])
                    else:
                        raise ValueError(f"Resource '{resource_name}' not found")
            except DatabaseError as err:
                raise RuntimeError("Database error occurred during get_data_details") from err
