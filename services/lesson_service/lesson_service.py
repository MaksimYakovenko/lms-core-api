from fastapi import HTTPException, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from models.lesson_model import Lesson
from models.journal_model import Journal
from models.classroom_model import Classroom
from core.constants import LessonType, LESSON_TYPE_LABELS
from repositories.lesson_repository import LessonRepository


class LessonService:

    @staticmethod
    async def add_lesson(
            db: AsyncSession,
            journal_id: int,
            lesson_date: date,
            lesson_type: LessonType = LessonType.LECTURE,
            classroom_id: int | None = None,
            lesson_number: int | None = None,
            title: str = "",
            description: str = "",
    ) -> Lesson:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Journal not found")

        res = await db.execute(
            select(func.max(Lesson.order_index)).where(
                Lesson.journal_id == journal_id)
        )
        max_order = res.scalar() or 0

        lesson = Lesson(
            journal_id=journal_id,
            date=lesson_date,
            lesson_type=lesson_type.value,
            order_index=max_order + 1,
            classroom_id=classroom_id,
            lesson_number=lesson_number,
            title=title,
            description=description,
        )
        res = await LessonRepository.create(db, lesson)
        await db.commit()
        await db.refresh(res)
        return res

    @staticmethod
    async def get_lessons(db: AsyncSession, journal_id: int) -> list[Lesson]:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Journal not found")

        return await LessonRepository.get_by_journal_id(db, journal_id)

    @staticmethod
    async def update_lesson(
            db: AsyncSession,
            journal_id: int,
            lesson_id: int,
            lesson_date: date | None = None,
            lesson_type: LessonType | None = None,
            classroom_id: int | None = None,
            lesson_number: int | None = None,
            title: str | None = None,
            description: str | None = None,
    ) -> Lesson:
        lesson = await LessonRepository.get_by_id_and_journal_id(db, lesson_id,
                                                                 journal_id)
        if lesson is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Lesson not found")

        if classroom_id is not None:
            classroom = await db.get(Classroom, classroom_id)
            if classroom is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Classroom not found")

        if lesson_date is not None:
            lesson.date = lesson_date
        if lesson_type is not None:
            lesson.lesson_type = lesson_type.value
        if classroom_id is not None:
            lesson.classroom_id = classroom_id
        if lesson_number is not None:
            lesson.lesson_number = lesson_number
        if title is not None:
            lesson.title = title
        if description is not None:
            lesson.description = description

        await LessonRepository.update(db, lesson)
        await db.commit()
        await db.refresh(lesson)
        return lesson

    @staticmethod
    async def delete_lesson(db: AsyncSession, journal_id: int,
                            lesson_id: int) -> None:
        lesson = await LessonRepository.get_by_id_and_journal_id(db, lesson_id,
                                                                 journal_id)
        if lesson is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Lesson not found")
        await LessonRepository.delete(db, lesson)
        await db.commit()

    @staticmethod
    async def get_lesson_types() -> list[dict]:
        return [
            {"value": lt.value, "label": LESSON_TYPE_LABELS[lt]}
            for lt in LessonType
        ]

    @staticmethod
    async def get_lesson_periods() -> list[dict]:
        return [
            {
                "number": 1,
                "label": "1 пара",
                "start_time": "08:40",
                "end_time": "10:15",
            },
            {
                "number": 2,
                "label": "2 пара",
                "start_time": "10:35",
                "end_time": "12:10",
            },
            {
                "number": 3,
                "label": "3 пара",
                "start_time": "12:20",
                "end_time": "13:55",
            },
            {
                "number": 4,
                "label": "4 пара",
                "start_time": "14:05",
                "end_time": "15:35",
            },
        ]


lesson_service = LessonService()
