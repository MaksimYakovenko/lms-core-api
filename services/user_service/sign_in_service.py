from models.auth_model import User
from utils.jwt import create_access_token
from utils.security import verify_password
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class SignInService:
    @staticmethod
    async def sign_in(db: AsyncSession, *, email: str, password: str) -> str:
        res = await db.execute(select(User).where(User.email == email))
        user = res.scalar_one_or_none()
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        token = create_access_token({"sub": user.email})
        return token


sign_in_service = SignInService()
