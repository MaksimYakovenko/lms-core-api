from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.auth_model import User


class UserRepository:
    @staticmethod
    async def create(db: AsyncSession, user: User) -> User:
        db.add(user)
        await db.flush()
        return user

    @staticmethod
    async def get_by_email(db: AsyncSession, email: str) -> User | None:
        res = await db.execute(select(User).where(User.email == email))
        user = res.scalar_one_or_none()
        return user
