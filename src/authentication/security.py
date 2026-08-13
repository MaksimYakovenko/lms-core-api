from __future__ import annotations

from datetime import datetime, timedelta
from typing import Callable
from fastapi import HTTPException, Request
from fastapi.middleware.base import BaseHTTPMiddleware
from collections import defaultdict
import logging

logger = logging.getLogger("security")

# Helper to validate tokens
def is_valid_token(token: str) -> bool:
    # Example valid token check
    return token == "VALID_TOKEN"

# Async logging function
async def log_unauthorized_access(attempt_info: str) -> None:
    """Logs unauthorized access attempts."""
    logger.warning(attempt_info)

class SecurityMiddleware(BaseHTTPMiddleware):
    """Custom security middleware to handle token validation and rate limiting."""

    RATE_LIMIT: int = 5
    TIME_FRAME: timedelta = timedelta(minutes=1)

    def __init__(self, app):
        super().__init__(app)
        self.requests_mapping: defaultdict[str, list[datetime]] = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        # Obtain client IP and token from headers
        token = request.headers.get("Authorization", "").removeprefix("Bearer ")
        ip_address = request.client.host
        # Rate limiting logic
        now = datetime.utcnow()
        self.requests_mapping[ip_address] = [req_time for req_time in self.requests_mapping[ip_address] if req_time > now - self.TIME_FRAME]
        if len(self.requests_mapping[ip_address]) >= self.RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Rate limit exceeded.")
        self.requests_mapping[ip_address].append(now)
        # Token validation
        if not is_valid_token(token):
            await log_unauthorized_access(f"Unauthorized access from {ip_address} with token={token!r}")
            raise HTTPException(status_code=401, detail="Invalid or expired token.")
        # Proceed to the next middleware or endpoint
        response = await call_next(request)
        return response
# Integration section
# Further integration into app as needed
