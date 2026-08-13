from __future__ import annotations

import os
import jwt
import pytest
from fastapi import HTTPException, Request, Response
from fastapi.testclient import TestClient
from typing import Awaitable, Callable
from src.auth.middleware import authentication_middleware

class MockRequest:
    def __init__(self, headers: dict[str, str]):
        self.headers = headers
        self.state = type("State", (), {})()  # Mock the state attribute.

@pytest.mark.asyncio
async def test_authentication_middleware_success() -> None:
    secret = "test_secret"
    os.environ["JWT_SECRET"] = secret
    valid_token = jwt.encode({"user_id": "12345"}, secret, algorithm="HS256")
    request = MockRequest({"Authorization": valid_token})

    async def mock_call_next(req: Request) -> Response:
        assert hasattr(req.state, "user_id")
        assert req.state.user_id == "12345"
        return Response(status_code=200)

    response = await authentication_middleware(request, mock_call_next)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_authentication_middleware_missing_token() -> None:
    request = MockRequest({})
    
    async def mock_call_next(req: Request) -> Response:
        return Response(status_code=200)

    with pytest.raises(HTTPException) as excinfo:
        await authentication_middleware(request, mock_call_next)
    assert excinfo.value.status_code == 403
    assert excinfo.value.detail == "Authorization header is missing."

@pytest.mark.asyncio
async def test_authentication_middleware_invalid_token() -> None:
    secret = "test_secret"
    os.environ["JWT_SECRET"] = secret
    invalid_token = "invalid_token"
    request = MockRequest({"Authorization": invalid_token})

    async def mock_call_next(req: Request) -> Response:
        return Response(status_code=200)

    with pytest.raises(HTTPException) as excinfo:
        await authentication_middleware(request, mock_call_next)
    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Invalid token."
