import pytest
from unittest.mock import MagicMock
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from src.middleware.jwt_auth import jwt_auth_middleware

@pytest.mark.asyncio
async def test_jwt_auth_middleware_invalid_header():
    """Test that the middleware raises an HTTPException for missing Authorization header."""
    mock_request = MagicMock(spec=Request)
    mock_request.headers = {}

    mock_call_next = MagicMock()

    with pytest.raises(HTTPException) as exc_info:
        await jwt_auth_middleware(mock_request, mock_call_next)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Missing or invalid Authorization header"