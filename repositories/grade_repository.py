from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.grade_model import Grade
from models.lesson_model import Lesson


class GradeRepository:
    @staticmethod
    async def upsert(db: AsyncSession, grade):
        db.add(grade)
        await db.flush()
        return grade

    @staticmethod
    async def get_by_lesson_and_student(db: AsyncSession, lesson_id: int, student_id: int) -> Grade | None:
        res = await db.execute(
            select(Grade).where(
                Grade.lesson_id == lesson_id,
                Grade.student_id == student_id,
            )
        )
        grade = res.scalar_one_or_none()
        return grade

    @staticmethod
    async def get_by_lesson_ids(db: AsyncSession, lesson_ids: list[int]) -> list[Grade]:
        if not lesson_ids:
            return []
        res = await db.execute(
            select(Grade).where(Grade.lesson_id.in_(lesson_ids))
        )
        grades = res.scalars().all()
        return grades

    @staticmethod
    async def get_by_id_and_journal_id(db: AsyncSession, grade_id: int, journal_id: int) -> Grade | None:
        res = await db.execute(
            select(Grade)
            .join(Lesson, Grade.lesson_id == Lesson.id)
            .where(Grade.id == grade_id, Lesson.journal_id == journal_id)
        )
        grade = res.scalar_one_or_none()
        return grade

    @staticmethod
    async def delete(db: AsyncSession, grade: Grade):
        await db.delete(grade)
        await db.flush()
