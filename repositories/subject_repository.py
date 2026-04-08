from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.subject_model import Subjects


class SubjectRepository:
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Subjects]:
        res = await db.execute(select(Subjects))
        subjects = res.scalars().all()
        return subjects

    @staticmethod
    async def get_by_id(db: AsyncSession, subject_id: int) -> Subjects | None:
        res = await db.execute(
            select(Subjects).where(Subjects.id == subject_id))
        subject = res.scalar_one_or_none()
        return subject

    @staticmethod
    async def create(db: AsyncSession, subject: Subjects) -> Subjects:
        db.add(subject)
        await db.flush()
        return subject

    @staticmethod
    async def delete(db: AsyncSession, subject: Subjects):
        await db.delete(subject)
        await db.flush()

    @staticmethod
    async def update(db: AsyncSession, subject: Subjects):
        db.add(subject)
        await db.flush()

    @staticmethod
    async def get_by_name(db: AsyncSession, name: str) -> Subjects | None:
        res = await db.execute(
            select(Subjects).where(Subjects.name == name))
        subject = res.scalar_one_or_none()
        return subject
