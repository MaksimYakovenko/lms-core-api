from __future__ import annotations

from typing import Any
from fastapi import HTTPException
from asyncpg import Pool

class ProfileHandler:
    """
    A class to handle profile related operations.
    """
    def __init__(self, db_pool: Pool) -> None:
        """
        Initializes the ProfileHandler with the database connection pool.

        Args:
            db_pool (Pool): Database connection pool
        """
        self.db_pool = db_pool

    async def get_user_profile(self, user_id: str, requested_user_id: str) -> dict[str, Any]:
        """
        Retrieve a user's profile after validating access.

        Args:
            user_id (str): ID of the user performing the request.
            requested_user_id (str): ID of the profile being requested.

        Returns:
            dict[str, Any]: User profile details.
            
        Raises:
            HTTPException: If user attempts to access a profile other than their own.
        """
        if user_id != requested_user_id:
            raise HTTPException(status_code=403, detail="Access denied: Cannot retrieve another user's profile.")
        async with self.db_pool.acquire() as connection:
            query = "SELECT * FROM public.user_profiles WHERE user_id = $1"
            profile = await connection.fetchrow(query, user_id)
            if profile is None:
                raise HTTPException(status_code=404, detail="Profile not found.")
            return dict(profile)

# Example usage and injection:
# from asyncpg import create_pool
# db_pool = create_pool(DATABASE_URL)
# profile_handler = ProfileHandler(db_pool)
# profile = await profile_handler.get_user_profile(current_user_id, requested_user_id)
