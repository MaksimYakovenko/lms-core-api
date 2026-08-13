from __future__ import annotations

import pytest
import asyncpg
from unittest.mock import AsyncMock, MagicMock

from src.user.profile_utils import UserProfileDataAccessLayer

@pytest.mark.asyncio
async def test_fetch_user_profile() -> None:
    """
    Test the fetch_user_profile method of UserProfileDataAccessLayer.
    """
    mock_pool = MagicMock()
    mock_connection = AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection

    asyncpg.create_pool = AsyncMock(return_value=mock_pool)

    mock_connection.fetchrow.return_value = {"id": 1, "name": "Test User"}

    dal = UserProfileDataAccessLayer(dsn="test_dsn")

    profile = await dal.fetch_user_profile(user_id=1)

    assert profile == {"id": 1, "name": "Test User"}
    mock_connection.fetchrow.assert_called_once_with("""
        SELECT *
        FROM users
        WHERE id = $1
    """, 1)

@pytest.mark.asyncio
async def test_fetch_user_profile_not_found() -> None:
    """
    Test the fetch_user_profile method raises an error for non-existent users.
    """
    mock_pool = MagicMock()
    mock_connection = AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection

    asyncpg.create_pool = AsyncMock(return_value=mock_pool)

    mock_connection.fetchrow.return_value = None

    dal = UserProfileDataAccessLayer(dsn="test_dsn")

    with pytest.raises(ValueError, match="User with ID 1 not found."):
        await dal.fetch_user_profile(user_id=1)

    mock_connection.fetchrow.assert_called_once_with("""
        SELECT *
        FROM users
        WHERE id = $1
    """, 1)
