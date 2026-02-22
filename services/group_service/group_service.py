from sqlalchemy.ext.asyncio import AsyncSession
from models.group_model import Groups


class GroupService:
    @staticmethod
    async def create_group(db: AsyncSession, name: str):
        group = Groups(name=name)
        db.add(group)
        await db.commit()
        await db.refresh(group)
        return group

    @staticmethod
    async def get_groups(db: AsyncSession) -> list[Groups]:
        res = await db.execute(select(Groups))
        groups = res.scalars().all()
        return groups


group_service = GroupService()
