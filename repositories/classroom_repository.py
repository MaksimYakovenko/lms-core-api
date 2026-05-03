from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.classroom_model import Classroom


class ClassroomRepository:
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Classroom]:
        res = await db.execute(select(Classroom))
        classrooms = res.scalars().all()
        return classrooms

    @staticmethod
    async def get_by_id(db: AsyncSession, classroom_id: int) -> Classroom | None:
        res = await db.execute(
            select(Classroom).where(Classroom.id == classroom_id))
        classroom = res.scalar_one_or_none()
        return classroom

    @staticmethod
    async def delete(db: AsyncSession, classroom: Classroom):
        await db.delete(classroom)
        await db.flush()

    @staticmethod
    async def create(db: AsyncSession, classroom: Classroom) -> Classroom:
        db.add(classroom)
        await db.flush()
        return classroom

    @staticmethod
    async def update(db: AsyncSession, classroom: Classroom):
        db.add(classroom)
        await db.flush()
