from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.grade_model import Grade
from models.lesson_model import Lesson
from models.student_model import Students
from schemas.grades import GradeUpsertRequest


class GradeService:

    @staticmethod
    async def upsert_grade(
        db: AsyncSession,
        journal_id: int,
        data: GradeUpsertRequest,
    ) -> Grade:
        # Перевірка що урок належить журналу
        lesson_res = await db.execute(
            select(Lesson).where(
                Lesson.id == data.lesson_id,
                Lesson.journal_id == journal_id,
            )
        )
        if lesson_res.scalar_one_or_none() is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Lesson not found in this journal",
            )

        # Перевірка студента
        student = await db.get(Students, data.student_id)
        if student is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

        # Upsert: знаходимо або створюємо
        existing_res = await db.execute(
            select(Grade).where(
                Grade.lesson_id == data.lesson_id,
                Grade.student_id == data.student_id,
            )
        )
        grade = existing_res.scalar_one_or_none()

        if grade is None:
            grade = Grade(
                lesson_id=data.lesson_id,
                student_id=data.student_id,
                value=data.value,
                remark=data.remark,
            )
            db.add(grade)
        else:
            grade.value = data.value
            grade.remark = data.remark
            db.add(grade)

        await db.commit()
        await db.refresh(grade)
        return grade

    @staticmethod
    async def bulk_upsert_grades(
        db: AsyncSession,
        journal_id: int,
        grades_data: list[GradeUpsertRequest],
    ) -> list[Grade]:
        results = []
        for item in grades_data:
            grade = await GradeService.upsert_grade(db, journal_id, item)
            results.append(grade)
        return results

    @staticmethod
    async def get_grades(db: AsyncSession, journal_id: int) -> list[Grade]:
        # Отримуємо всі оцінки по уроках цього журналу
        lessons_res = await db.execute(
            select(Lesson.id).where(Lesson.journal_id == journal_id)
        )
        lesson_ids = [row[0] for row in lessons_res.fetchall()]

        if not lesson_ids:
            return []

        grades_res = await db.execute(
            select(Grade).where(Grade.lesson_id.in_(lesson_ids))
        )
        return grades_res.scalars().all()

    @staticmethod
    async def delete_grade(db: AsyncSession, journal_id: int, grade_id: int) -> None:
        # Перевіряємо що grade належить цьому журналу
        res = await db.execute(
            select(Grade)
            .join(Lesson, Grade.lesson_id == Lesson.id)
            .where(Grade.id == grade_id, Lesson.journal_id == journal_id)
        )
        grade = res.scalar_one_or_none()
        if grade is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grade not found")

        await db.delete(grade)
        await db.commit()


grade_service = GradeService()
