from __future__ import annotations

from jwt import decode, DecodeError
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import asyncpg
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

def get_database_pool():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL must be set")
    return asyncpg.create_pool(dsn=db_url)

async def retrieve_user_profile(user_id: str) -> dict:
    pool = get_database_pool()
    async with pool.acquire() as conn:
        user_query = 'SELECT * FROM users WHERE id = $1;'
        result = await conn.fetchrow(user_query, int(user_id))
        if result is None:
            raise HTTPException(status_code=404, detail="User profile not found")
        return dict(result)

def decode_jwt_token(token: str) -> dict:
    try:
        secret = os.getenv("JWT_SECRET")
        if not secret:
            raise RuntimeError("JWT_SECRET must be set")
        return decode(token, key=secret, algorithms=["HS256"])
    except DecodeError as e:
        raise HTTPException(status_code=401, detail="Invalid JWT token") from e

@router.get("/profile", response_model=dict)
async def get_profile(token: str = Depends(oauth2_scheme)) -> dict:
    payload = decode_jwt_token(token)
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Missing user ID in token")

    profile = await retrieve_user_profile(user_id)
    return profile
