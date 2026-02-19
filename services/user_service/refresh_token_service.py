from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.auth_model import User
from utils.jwt import verify_refresh_token, create_access_token, \
    create_refresh_token


class RefreshTokenService:
    @staticmethod
    async def refresh(db: AsyncSession, *, refresh_token: str) -> dict:
        user_id = verify_refresh_token(refresh_token)
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )

        res = await db.execute(select(User).where(User.id == int(user_id)))
        user = res.scalar_one_or_none()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        new_access_token = create_access_token(str(user.id))
        new_refresh_token = create_refresh_token(str(user.id))

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token
        }


refresh_token_service = RefreshTokenService()
