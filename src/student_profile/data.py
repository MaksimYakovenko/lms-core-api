from __future__ import annotations

import os
import asyncpg
from typing import Any

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Environment variable DATABASE_URL is not set.")

class StudentDataAccess:
    """Handles database operations for student profiles."""

    def __init__(self) -> None:
        self.pool: asyncpg.Pool | None = None

    async def initialize(self) -> None:
        """Initializes the connection pool."""
        self.pool = await asyncpg.create_pool(DATABASE_URL)

    async def close(self) -> None:
        """Closes the connection pool."""
        if self.pool:
            await self.pool.close()

    async def get_student_profile(self, student_id: int) -> dict[str, Any] | None:
        """Fetches a student's profile by their student ID. Returns None if not found."""
        if not self.pool:
            raise ValueError("Connection pool is not initialized.")
        async with self.pool.acquire() as connection:
            query = """
                SELECT * FROM students WHERE id = $1;
            """
            result = await connection.fetchrow(query, student_id)
            if result:
                return dict(result)
            return None
