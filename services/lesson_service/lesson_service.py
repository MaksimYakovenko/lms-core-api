from fastapi import HTTPException, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from models.lesson_model import Lesson
from models.journal_model import Journal
from core.constants import LessonType


class LessonService:

    @staticmethod
    async def add_lesson(
        db: AsyncSession,
        journal_id: int,
        lesson_date: date,
        lesson_type: LessonType = LessonType.LESSON,
        topic: str | None = None,
    ) -> Lesson:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal not found")

        # Визначаємо наступний order_index
        res = await db.execute(
            select(func.max(Lesson.order_index)).where(Lesson.journal_id == journal_id)
        )
        max_order = res.scalar() or 0

        lesson = Lesson(
            journal_id=journal_id,
            date=lesson_date,
            lesson_type=lesson_type.value,
            order_index=max_order + 1,
            topic=topic,
        )
        db.add(lesson)
        await db.commit()
        await db.refresh(lesson)
        return lesson

    @staticmethod
    async def get_lessons(db: AsyncSession, journal_id: int) -> list[Lesson]:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal not found")

        res = await db.execute(
            select(Lesson)
            .where(Lesson.journal_id == journal_id)
            .order_by(Lesson.order_index)
        )
        return res.scalars().all()

    @staticmethod
    async def update_lesson(
        db: AsyncSession,
        journal_id: int,
        lesson_id: int,
        lesson_date: date | None = None,
        lesson_type: LessonType | None = None,
        topic: str | None = None,
    ) -> Lesson:
        res = await db.execute(
            select(Lesson).where(Lesson.id == lesson_id, Lesson.journal_id == journal_id)
        )
        lesson = res.scalar_one_or_none()
        if lesson is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")

        if lesson_date is not None:
            lesson.date = lesson_date
        if lesson_type is not None:
            lesson.lesson_type = lesson_type.value
        if topic is not None:
            lesson.topic = topic

        db.add(lesson)
        await db.commit()
        await db.refresh(lesson)
        return lesson

    @staticmethod
    async def delete_lesson(db: AsyncSession, journal_id: int, lesson_id: int) -> None:
        res = await db.execute(
            select(Lesson).where(Lesson.id == lesson_id, Lesson.journal_id == journal_id)
        )
        lesson = res.scalar_one_or_none()
        if lesson is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
        await db.delete(lesson)
        await db.commit()


lesson_service = LessonService()
