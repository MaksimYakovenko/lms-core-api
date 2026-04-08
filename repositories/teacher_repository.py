from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.teacher_model import Teachers


class TeacherRepository:
    @staticmethod
    async def create(db: AsyncSession, teacher: Teachers) -> Teachers:
        db.add(teacher)
        await db.flush()
        return teacher

    @staticmethod
    async def get_all(db: AsyncSession) -> list[Teachers]:
        res = await db.execute(select(Teachers))
        teachers = res.scalars().all()
        return teachers

    @staticmethod
    async def get_by_id(db: AsyncSession, teacher_id: int) -> Teachers | None:
        res = await db.execute(
            select(Teachers).where(Teachers.id == teacher_id))
        teacher = res.scalar_one_or_none()
        return teacher

    @staticmethod
    async def get_by_email(db: AsyncSession, email: str) -> Teachers | None:
        res = await db.execute(
            select(Teachers).where(Teachers.email == email))
        teacher = res.scalar_one_or_none()
        return teacher

    @staticmethod
    async def delete(db: AsyncSession, teacher: Teachers):
        await db.delete(teacher)
        await db.flush()

    @staticmethod
    async def update(db: AsyncSession, teacher: Teachers):
        db.add(teacher)
        await db.flush()
