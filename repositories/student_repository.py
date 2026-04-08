from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.student_model import Students


class StudentRepository:
    @staticmethod
    async def create(db: AsyncSession, student: Students) -> Students:
        db.add(student)
        await db.flush()
        return student

    @staticmethod
    async def get_all(db: AsyncSession) -> list[Students]:
        res = await db.execute(select(Students))
        students = res.scalars().all()
        return students

    @staticmethod
    async def get_by_id(db: AsyncSession, student_id: int) -> Students | None:
        res = await db.execute(
            select(Students).where(Students.id == student_id))
        student = res.scalar_one_or_none()
        return student

    @staticmethod
    async def delete(db: AsyncSession, student: Students):
        await db.delete(student)
        await db.flush()


    @staticmethod
    async def update(db: AsyncSession, student: Students):
        db.add(student)
        await db.flush()


