from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.admin_model import Admins


class AdminRepository:
    @staticmethod
    async def create(db: AsyncSession, admin: Admins) -> Admins:
        db.add(admin)
        await db.flush()
        return admin

    @staticmethod
    async def get_all(db: AsyncSession) -> list[Admins]:
        res = await db.execute(select(Admins))
        admins = res.scalars().all()
        return admins

    @staticmethod
    async def get_by_id(db: AsyncSession, admin_id: int) -> Admins:
        res = await db.execute(
            select(Admins).where(Admins.id == admin_id))
        admin = res.scalar_one_or_none()
        return admin

    @staticmethod
    async def delete(db: AsyncSession, admin: Admins):
        await db.delete(admin)
        await db.flush()

    @staticmethod
    async def get_by_email(db: AsyncSession, email: str) -> Admins | None:
        res = await db.execute(
            select(Admins).where(Admins.email == email))
        admin = res.scalar_one_or_none()
        return admin

    @staticmethod
    async def update(db: AsyncSession, admin: Admins):
        db.add(admin)
        await db.flush()
