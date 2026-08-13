from __future__ import annotations

from typing import Awaitable, Callable
import os
import jwt
from fastapi import HTTPException, Request, Response

def get_jwt_secret() -> str:
    """Retrieve the JWT secret from environment variable."""
    secret = os.getenv("JWT_SECRET")
    if not secret:
        raise EnvironmentError("JWT_SECRET is not set in the environment variables.")
    return secret

async def authentication_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Middleware to authenticate incoming requests using JWT tokens."""
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=403, detail="Authorization header is missing.")
    try:
        payload = jwt.decode(token, get_jwt_secret(), algorithms=["HS256"])
        request.state.user_id = payload.get("user_id")
    except jwt.PyJWTError as error:
        raise HTTPException(status_code=401, detail="Invalid token.") from error
    return await call_next(request)
