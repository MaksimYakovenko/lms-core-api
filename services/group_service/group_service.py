from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.group_model import Groups
from models.teacher_model import teacher_groups
from repositories.group_repository import GroupRepository
from sqlalchemy.future import select


class GroupService:
    @staticmethod
    async def create_group(db: AsyncSession, name: str, course_number: int) \
            -> Groups:
        res = await db.execute(
            select(Groups).where(
                (Groups.name == name) & (Groups.course_number == course_number)
            )
        )
        if res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Group already exists"
            )

        group = Groups(name=name, course_number=course_number)
        return await GroupRepository.create(db, group)

    @staticmethod
    async def get_groups(db: AsyncSession) -> list[Groups]:
        return await GroupRepository.get_all(db)

    @staticmethod
    async def delete_group(db: AsyncSession, group_id: int):
        group = await GroupRepository.get_by_id(db, group_id)
        if group is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Group not found"
            )
        await GroupRepository.delete(db, group)

    @staticmethod
    async def update_group(db: AsyncSession, group_id: int, name: str,
                           course_number: int):
        group = await GroupRepository.get_by_id(db, group_id)
        if group is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Group not found"
            )
        group.name = name
        group.course_number = course_number
        await GroupRepository.update(db, group)

    @staticmethod
    async def get_my_groups(db: AsyncSession, teacher_id: int) -> list[Groups]:
        res = await db.execute(
            select(Groups).join(
                teacher_groups, teacher_groups.c.group_id == Groups.id
            ).where(teacher_groups.c.teacher_id == teacher_id)
        )
        return res.scalars().all()


group_service = GroupService()
