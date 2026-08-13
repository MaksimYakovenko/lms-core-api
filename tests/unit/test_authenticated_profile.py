import pytest
from unittest.mock import AsyncMock, patch
from fastapi import HTTPException
from src.endpoints.authenticated_profile import decode_jwt_token, retrieve_user_profile, get_profile

@pytest.mark.asyncio
async def test_decode_jwt_token_valid_token():
    valid_token = "valid.jwt.token"
    expected_payload = {"user_id": "1234"}
    with patch("src.endpoints.authenticated_profile.decode", return_value=expected_payload):
        result = decode_jwt_token(valid_token)
        assert result == expected_payload

@pytest.mark.asyncio
async def test_decode_jwt_token_invalid_token():
    invalid_token = "invalid.jwt.token"
    with patch("src.endpoints.authenticated_profile.decode", side_effect=HTTPException(status_code=401, detail="Invalid JWT token")):
        with pytest.raises(HTTPException) as exc_info:
            decode_jwt_token(invalid_token)
        assert exc_info.value.status_code == 401

@pytest.mark.asyncio
async def test_retrieve_user_profile_valid_user():
    user_id = "12345"
    user_profile = {"id": 12345, "name": "John Doe", "email": "john.doe@example.com"}
    async_pool = AsyncMock()
    async_pool.acquire.return_value.fetchrow.return_value = user_profile
    with patch("src.endpoints.authenticated_profile.get_database_pool", return_value=async_pool):
        result = await retrieve_user_profile(user_id)
        assert result == user_profile

@pytest.mark.asyncio
async def test_retrieve_user_profile_invalid_user():
    user_id = "invalid"  # Cannot be parsed to an integer
    with pytest.raises(HTTPException) as exc_info:
        await retrieve_user_profile(user_id)
    assert exc_info.value.status_code == 400

@pytest.mark.asyncio
async def test_get_profile_valid_request():
    token = "valid.jwt.token"
    payload = {"user_id": "12345"}
    user_profile = {"id": 12345, "name": "John Doe", "email": "john.doe@example.com"}
    async_pool = AsyncMock()
    async_pool.acquire.return_value.fetchrow.return_value = user_profile
    with patch("src.endpoints.authenticated_profile.decode", return_value=payload), patch("src.endpoints.authenticated_profile.get_database_pool", return_value=async_pool):
        result = await get_profile(token)
        assert result == user_profile

@pytest.mark.asyncio
async def test_get_profile_missing_user_id():
    token = "invalid.jwt.token"
    payload = {}
    async_pool = AsyncMock()
    async_pool.acquire.return_value.fetchrow.return_value = None
    with patch("src.endpoints.authenticated_profile.decode", return_value=payload):
        with pytest.raises(HTTPException) as exc_info:
            await get_profile(token)
        assert exc_info.value.status_code == 401