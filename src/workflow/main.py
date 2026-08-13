from __future__ import annotations

from fastapi import APIRouter, Depends
from asyncpg import connect, Connection
import os

async def get_student_profile(student_id: int) -> dict:
    """
    This async method retrieves a student's profile based on their ID.

    Args:
        student_id (int): The unique ID of the student

    Returns:
        dict: The profile of the student.
    """
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable not set")

    async with connect(database_url) as connection:
        query = """
        SELECT *
        FROM public.profiles
        WHERE student_id = $1
        LIMIT 1
        """
        result = await connection.fetchrow(query, student_id)
        if result is None:
            raise ValueError(f"Student profile with ID {student_id} not found")
        return dict(result)

router = APIRouter()

@router.get("/student/{student_id}/profile")
async def profile_endpoint(student_id: int) -> dict[str, str]:
    """
    This endpoint retrieves the student profile based on student ID.

    Args:
        student_id (int): The unique ID of the student

    Returns:
        dict[str, str]: Dict containing profile details.
    """
    return await get_student_profile(student_id)
