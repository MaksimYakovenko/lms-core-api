import pytest
from unittest.mock import AsyncMock, patch
from datetime import datetime, timedelta
from fastapi import HTTPException
from fastapi.middleware.base import BaseHTTPMiddleware
from src.authentication.security import SecurityMiddleware, is_valid_token, log_unauthorized_access

@pytest.mark.asyncio
async def test_valid_token_allows_request():
    """Test that valid token allows the request to pass."""
    app_mock = AsyncMock()
    middleware = SecurityMiddleware(app_mock)
    request_mock = AsyncMock()
    request_mock.headers = {"Authorization": "Bearer VALID_TOKEN"}
    request_mock.client.host = "127.0.0.1"

    with patch("src.authentication.security.is_valid_token", return_value=True):
        with patch("src.authentication.security.log_unauthorized_access") as log_mock:
            await middleware.dispatch(request_mock, app_mock)
            log_mock.assert_not_called()

@pytest.mark.asyncio
async def test_invalid_token_raises_http_exception():
    """Test that an invalid token raises HTTPException."""
    app_mock = AsyncMock()
    middleware = SecurityMiddleware(app_mock)
    request_mock = AsyncMock()
    request_mock.headers = {"Authorization": "Bearer INVALID_TOKEN"}
    request_mock.client.host = "127.0.0.1"

    with patch("src.authentication.security.is_valid_token", return_value=False):
        with patch("src.authentication.security.log_unauthorized_access") as log_mock:
            with pytest.raises(HTTPException) as exc_info:
                await middleware.dispatch(request_mock, app_mock)
            assert exc_info.value.status_code == 401
            log_mock.assert_called_once_with("Unauthorized access from 127.0.0.1 with token='INVALID_TOKEN'")

@pytest.mark.asyncio
async def test_rate_limit_exceeded_raises_http_exception():
    """Test that exceeding rate limit raises HTTPException."""
    app_mock = AsyncMock()
    middleware = SecurityMiddleware(app_mock)
    middleware.requests_mapping = {"127.0.0.1": [datetime.utcnow() for _ in range(middleware.RATE_LIMIT)]}

    request_mock = AsyncMock()
    request_mock.headers = {"Authorization": "Bearer VALID_TOKEN"}
    request_mock.client.host = "127.0.0.1"

    with pytest.raises(HTTPException) as exc_info:
        await middleware.dispatch(request_mock, app_mock)
    assert exc_info.value.status_code == 429