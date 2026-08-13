import pytest
import unittest.mock as mock
from fastapi import HTTPException
from src.student_service import get_student_profile

@pytest.mark.asyncio
async def test_get_student_profile_valid():
    """
    Test the `get_student_profile` function with valid input,
    mocking database interactions to simulate a successful response.
    """
    # Arrange
    mocked_pool = mock.Mock()
    mocked_connection = mock.Mock()
    mocked_pool.acquire.return_value.__aenter__.return_value = mocked_connection
    mocked_connection.fetchrow.return_value = {
        "id": 123,
        "name": "John Doe",
        "age": 20
    }
    mocked_connection.fetch.return_value = [
        {"course_name": "Math"},
        {"course_name": "Science"}
    ]

    with mock.patch("asyncpg.create_pool", return_value=mocked_pool):
        # Act
        result = await get_student_profile(student_id=123)

        # Assert
        assert result == {
            "id": 123,
            "name": "John Doe",
            "age": 20,
            "courses": ["Math", "Science"]
        }

@pytest.mark.asyncio
async def test_get_student_profile_invalid_id():
    """
    Test the `get_student_profile` function for a non-existent student ID,
    expecting a 404 error.
    """
    # Arrange
    mocked_pool = mock.Mock()
    mocked_connection = mock.Mock()
    mocked_pool.acquire.return_value.__aenter__.return_value = mocked_connection
    mocked_connection.fetchrow.return_value = None

    with mock.patch("asyncpg.create_pool", return_value=mocked_pool):
        # Act/Assert
        with pytest.raises(HTTPException) as exc_info:
            await get_student_profile(student_id=999)
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Student profile not found."

@pytest.mark.asyncio
async def test_get_student_profile_missing_env_var():
    """
    Test the `get_student_profile` function when the `DATABASE_URL` environment
    variable is not set, expecting a 500 error.
    """
    # Arrange
    with mock.patch.dict("os.environ", {}):
        # Act/Assert
        with pytest.raises(HTTPException) as exc_info:
            await get_student_profile(student_id=123)
        assert exc_info.value.status_code == 500
        assert exc_info.value.detail == "Database URL not configured."