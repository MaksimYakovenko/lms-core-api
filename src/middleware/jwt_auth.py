from __future__ import annotations

import os
import jwt
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Callable, Awaitable
async def jwt_auth_middleware(request: Request, call_next: Callable[[Request], Awaitable[JSONResponse]]) -> JSONResponse:
    """Middleware to authenticate using JWT for protected routes."""
    try:
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
        token = auth_header[len("Bearer "):].strip()
        secret = os.environ.get("JWT_SECRET")
        if not secret:
            raise HTTPException(status_code=500, detail="Server misconfiguration: missing secret key")
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        request.state.user = payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Unknown error occurred") from exc

    return await call_next(request)
