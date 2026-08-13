from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, DecodeError
import asyncpg
import os

# Initialize FastAPI routing components
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

# Global singleton database pool
_pool: asyncpg.pool.Pool | None = None

async def get_database_pool() -> asyncpg.pool.Pool:
    """Ensure a singleton connection pool is established."""
    global _pool
    if _pool is None:
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise RuntimeError("DATABASE_URL environment variable not set")
        _pool = await asyncpg.create_pool(dsn=db_url)
    return _pool

# Retrieve JWT_SECRET once from environment
JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET environment variable not set")

def decode_jwt_token(token: str) -> dict[str, str | int]:
    """Decode and validate a JWT token."""
    try:
        return decode(token, key=JWT_SECRET, algorithms=["HS256"])
    except DecodeError as err:
        raise HTTPException(status_code=401, detail="Invalid JWT token") from err

async def retrieve_user_profile(user_id: str) -> dict[str, str | int | None]:
    """Query the user profile from the database."""
    if not user_id.isdigit():
        raise HTTPException(status_code=400, detail="Invalid user ID")
    pool = await get_database_pool()
    async with pool.acquire() as conn:
        user_query = 'SELECT id, name, email FROM users WHERE id = $1;'
        result = await conn.fetchrow(user_query, int(user_id))
        if result is None:
            raise HTTPException(status_code=404, detail="User profile not found")
        return dict(result)

@router.get("/profile", response_model=dict[str, str | int | None])
async def get_profile(token: str = Depends(oauth2_scheme)) -> dict[str, str | int | None]:
    """Retrieve authenticated user's profile."""
    payload = decode_jwt_token(token)
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Missing 'user_id' in token")
    return await retrieve_user_profile(user_id)
