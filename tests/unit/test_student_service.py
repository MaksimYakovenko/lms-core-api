from __future__ import annotations

import pytest
from src.student_service import get_student_profile
from unittest.mock import patch

@pytest.mark.asyncio
async def test_get_student_profile() -> None:
    """Unit tests for retrieving student profiles."""

    mock_student_id = 1
    expected_profile = {
        "id": mock_student_id,
        "name": "John Doe",
        "age": 20,
        "courses": ["Math", "Science"]
    }

    with patch("src.student_service.asyncpg.create_pool") as mock_pool:
        async def mock_fetchrow(query: str, value: int):
            return {"id": mock_student_id, "name": "John Doe", "age": 20}

        async def mock_fetch(query: str, value: int):
            return [{"course_name": "Math"}, {"course_name": "Science"}]

        mock_pool.return_value.acquire.return_value.fetchrow = mock_fetchrow
        mock_pool.return_value.acquire.return_value.fetch = mock_fetch

        actual_profile = await get_student_profile(mock_student_id)

        assert actual_profile == expected_profile
