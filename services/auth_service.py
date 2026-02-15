from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from utils.security import hash_password
from models.auth_model import User


async def create_user(db: AsyncSession, *, email: str, first_name: str,
                      last_name: str, password: str) -> User:
    res = await db.execute(select(User).where(User.email == email))
    if res.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=hash_password(password),
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
