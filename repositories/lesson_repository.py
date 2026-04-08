from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.lesson_model import Lesson


class LessonRepository:
    @staticmethod
    async def create(db: AsyncSession, lesson: Lesson) -> Lesson:
        db.add(lesson)
        await db.flush()
        return lesson

    @staticmethod
    async def get_all(db: AsyncSession) -> list[Lesson]:
        res = await db.execute(select(Lesson))
        lessons = res.scalars().all()
        return lessons

    @staticmethod
    async def get_by_id(db: AsyncSession, lesson_id: int) -> Lesson | None:
        res = await db.execute(
            select(Lesson).where(Lesson.id == lesson_id))
        lesson = res.scalar_one_or_none()
        return lesson

    @staticmethod
    async def delete(db: AsyncSession, lesson: Lesson):
        await db.delete(lesson)
        await db.flush()

    @staticmethod
    async def update(db: AsyncSession, lesson: Lesson):
        db.add(lesson)
        await db.flush()

    @staticmethod
    async def get_by_journal_id(db: AsyncSession, journal_id: int) -> list[Lesson]:
        res = await db.execute(
            select(Lesson)
            .where(Lesson.journal_id == journal_id)
            .order_by(Lesson.order_index)
        )
        lessons = res.scalars().all()
        return lessons

    @staticmethod
    async def get_by_id_and_journal_id(db: AsyncSession, lesson_id: int, journal_id: int) -> Lesson | None:
        res = await db.execute(
            select(Lesson).where(Lesson.id == lesson_id, Lesson.journal_id == journal_id)
        )
        lesson = res.scalar_one_or_none()
        return lesson
