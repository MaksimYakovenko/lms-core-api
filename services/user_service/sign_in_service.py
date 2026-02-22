from models.auth_model import User
from utils.jwt import create_access_token, create_refresh_token
from utils.security import verify_password
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from utils.extract_roles import update_last_login


class SignInService:
    @staticmethod
    async def sign_in(db: AsyncSession, *, email: str, password: str) -> dict:
        res = await db.execute(select(User).where(User.email == email))
        user = res.scalar_one_or_none()
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if user.status == "BLOCKED":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Your account has been blocked. Please contact administrator."
            )

        await update_last_login(db, user)

        await db.commit()

        access_token = create_access_token(str(user.id))
        refresh_token = create_refresh_token(str(user.id))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }


sign_in_service = SignInService()
