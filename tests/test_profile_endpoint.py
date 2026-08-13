from __future__ import annotations

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.backend_module.profile_endpoint import ProfileHandler

@pytest.mark.asyncio
async def test_get_user_profile_success() -> None:
    """
    Test retrieval of a user's own profile.
    """
    pool = MagicMock()
    connection = AsyncMock()
    pool.acquire = AsyncMock(return_value=connection)

    connection.fetchrow = AsyncMock(return_value={"user_id": "user123", "name": "Test User"})

    handler = ProfileHandler(pool)
    profile = await handler.get_user_profile("user123", "user123")

    assert profile == {"user_id": "user123", "name": "Test User"}
    connection.fetchrow.assert_called_once_with("SELECT * FROM public.user_profiles WHERE user_id = $1", "user123")

@pytest.mark.asyncio
async def test_get_user_profile_access_denied() -> None:
    """
    Test access denial when trying to fetch another user's profile.
    """
    pool = MagicMock()
    handler = ProfileHandler(pool)

    with pytest.raises(Exception) as exc:
        await handler.get_user_profile("user123", "otheruser")

    assert "Access denied" in str(exc.value)
