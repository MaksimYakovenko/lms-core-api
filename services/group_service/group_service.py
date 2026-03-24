from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.group_model import Groups
from sqlalchemy import select


class GroupService:
    @staticmethod
    async def create_group(db: AsyncSession, name: str, course_number: int):
        res = await db.execute(select(Groups).where(Groups.name == name))
        if res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Group already exists"
            )

        group = Groups(name=name, course_number=course_number)
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
