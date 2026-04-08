from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.group_model import Groups


class GroupRepository:
    @staticmethod
    async def create(db: AsyncSession, group: Groups) -> Groups:
        db.add(group)
        await db.flush()
        return group


    @staticmethod
    async def get_all(db: AsyncSession) -> list[Groups]:
        res = await db.execute(select(Groups))
        groups = res.scalars().all()
        return groups


    @staticmethod
    async def get_by_id(db: AsyncSession, group_id: int) -> Groups | None:
        res = await db.execute(
            select(Groups).where(Groups.id == group_id))
        group = res.scalar_one_or_none()
        return group
