from __future__ import annotations

## Import Statements
from datetime import datetime, timedelta
from typing import Callable
from fastapi import Header, HTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import logging
import asyncio
from collections import defaultdict

## Logger Configuration
logger = logging.getLogger("security")

def is_valid_token(token: str) -> bool:
    """Simple token validation example."""
    return token == "VALID_TOKEN"

async def fake_activity_log(message: str) -> None:
    """Log the given message asynchronously."""
    logger.info(message)

def obtain_current_time() -> datetime:
    """Retrieve the current timestamp."""
    return datetime.utcnow()

## Security Middleware
def create_security_middleware() -> Middleware:
    # Rate limiting configuration
    requests_mapping: defaultdict[str, list[datetime]] = defaultdict(list)
    request_limit: int = 5
    time_frame: timedelta = timedelta(minutes=1)

    async def security_middleware(request, call_next):
        # Extract token from authorization header, if present
        authorization: str = request.headers.get("authorization", "")
        token = authorization.replace("Bearer ", "")
        ip_address: str = request.client.host

        # Rate limit logic
        now = obtain_current_time()
        requests_mapping[ip_address] = [req for req in requests_mapping[ip_address] if req > now - time_frame]
        if len(requests_mapping[ip_address]) >= request_limit:
            raise HTTPException(status_code=429, detail="Rate limit exceeded.")
        requests_mapping[ip_address].append(now)

        # Token validation logic
        if not is_valid_token(token):
            await fake_activity_log(f"Unauthorized access attempt from {ip_address} with token={token!r}")
            raise HTTPException(status_code=401, detail="Invalid or expired token.")

        response = await call_next(request)
        return response

    return Middleware(create_security_middleware)

## Integration
middleware = create_security_middleware()
