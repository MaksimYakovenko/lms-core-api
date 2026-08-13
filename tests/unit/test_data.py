from __future__ import annotations

import pytest
import asyncpg
from src.student_profile.data import StudentDataAccess

@pytest.mark.asyncio
async def test_get_student_profile() -> None:
    """Tests fetching a student profile."""
    # Setup
    data_access = StudentDataAccess()

    await data_access.initialize()

    # Mock data
    student_id = 123

    async with data_access.pool.acquire() as connection:
        await connection.execute(
            "INSERT INTO students (id, name, age) VALUES ($1, $2, $3)",
            student_id, "John Doe", 20
        )

    # Test
    profile = await data_access.get_student_profile(student_id)
    assert profile is not None
    assert profile["id"] == student_id

    # Teardown
    await data_access.close()
