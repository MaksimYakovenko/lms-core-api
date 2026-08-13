import pytest
from unittest.mock import AsyncMock
from fastapi import HTTPException
from src.backend_module.profile_endpoint import ProfileHandler

@pytest.mark.asyncio
async def test_get_user_profile_access_own_profile():
    """
    Test that a user can access their own profile.
    """
    # Arrange
    user_id = "user1"
    requested_user_id = "user1"
    mocked_pool = AsyncMock()
    mocked_connection = AsyncMock()
    mocked_pool.acquire.return_value.__aenter__.return_value = mocked_connection
    mocked_connection.fetchrow.return_value = {"user_id": user_id, "name": "Test User"}
    ph = ProfileHandler(mocked_pool)
    # Act
    result = await ph.get_user_profile(user_id, requested_user_id)
    # Assert
    assert result == {"user_id": user_id, "name": "Test User"}

@pytest.mark.asyncio
async def test_get_user_profile_access_other_profile():
    """
    Test that trying to access another user's profile raises HTTPException.
    """
    # Arrange
    user_id = "user1"
    requested_user_id = "user2"
    mocked_pool = AsyncMock()
    ph = ProfileHandler(mocked_pool)
    # Act and Assert
    with pytest.raises(HTTPException) as exc_info:
        await ph.get_user_profile(user_id, requested_user_id)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "Access denied: Cannot retrieve another user's profile."

@pytest.mark.asyncio
async def test_get_user_profile_not_exists():
    """
    Test that trying to access a non-existent profile raises HTTPException.
    """
    # Arrange
    user_id = "user1"
    requested_user_id = "user1"
    mocked_pool = AsyncMock()
    mocked_connection = AsyncMock()
    mocked_pool.acquire.return_value.__aenter__.return_value = mocked_connection
    mocked_connection.fetchrow.return_value = None
    ph = ProfileHandler(mocked_pool)
    # Act and Assert
    with pytest.raises(HTTPException) as exc_info:
        await ph.get_user_profile(user_id, requested_user_id)
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Profile not found."