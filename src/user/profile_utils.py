from __future__ import annotations

import os

import asyncpg

class UserProfileDataAccessLayer:
    """
    A class designed to handle data access related to user profiles.
    """
    def __init__(self, dsn: str) -> None:
        """
        Initialize the data access layer.

        Args:
            dsn: The data source name (connection string) for the database.
        """
        self.dsn = dsn
    async def fetch_user_profile(self, user_id: int) -> dict[str, str]:
        """
        Fetch user profile data given a user ID.

        Args:
            user_id: The ID of the user to fetch profile data for.

        Returns:
            A dictionary with the user profile data.

        Raises:
            ValueError: If the user does not exist.
        """
        pool = await asyncpg.create_pool(dsn=self.dsn)
        async with pool.acquire() as connection:
            row = await connection.fetchrow("""
                SELECT *
                FROM users
                WHERE id = $1
            """, user_id)
            if row is None:
                raise ValueError(f"User with ID {user_id} not found.")
            return dict(row)
