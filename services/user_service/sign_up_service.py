from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from models.auth_model import User
from utils.security import hash_password
from services.user_service.captcha_service import captcha_service
from utils.extract_roles import extract_role


class SignUpService:
    @staticmethod
    async def create_user(db: AsyncSession,
                          *,
                          email: str,
                          first_name: str,
                          last_name: str,
                          password: str,
                          birthday: date,
                          captcha_id: str,
                          captcha_answer: str
                          ) -> User:
        await captcha_service.verify_captcha(captcha_id, captcha_answer)

        res = await db.execute(select(User).where(User.email == email))
        if res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        role = await extract_role(
            db,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=hash_password(password),
            birthday=birthday,
            role=role
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user


auth_service = SignUpService()
