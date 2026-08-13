from __future__ import annotations

import os
import pytest
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from src.middleware.jwt_auth import jwt_auth_middleware
import jwt

@pytest.mark.asyncio
async def test_jwt_auth_middleware() -> None:
    """Tests the JWT authentication middleware."""
    os.environ["JWT_SECRET"] = "secret"
    token = jwt.encode({"user_id": 123}, "secret", algorithm="HS256")
    
    class MockRequest:
        def __init__(self):
            self.headers = {"Authorization": f"Bearer {token}"}
            self.state = type("mock", (), {})()
    
    async def call_next(request: Request) -> JSONResponse:
        assert hasattr(request.state, "user")
        return JSONResponse(content={"message": "Success"})
    
    request = MockRequest()
    response = await jwt_auth_middleware(request, call_next)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_missing_token() -> None:
    """Tests JWT Middleware when no token is present."""
    os.environ["JWT_SECRET"] = "secret"
    
    class MockRequest:
        def __init__(self):
            self.headers = {}
            self.state = type("mock", (), {})()
    
    async def call_next(_: Request) -> JSONResponse:
        return JSONResponse(content={"message": "Success"})
    
    request = MockRequest()
    with pytest.raises(HTTPException) as exc:
        await jwt_auth_middleware(request, call_next)
    assert exc.value.status_code == 401
    assert exc.value.detail == "Missing or invalid Authorization header"
