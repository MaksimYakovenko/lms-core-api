from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.grade_model import Grade
from models.lesson_model import Lesson
from models.student_model import Students
from schemas.grades import GradeUpsertRequest
from repositories.grade_repository import GradeRepository


class GradeService:

    @staticmethod
    async def upsert_grade(
        db: AsyncSession,
        journal_id: int,
        data: GradeUpsertRequest,
    ) -> Grade:
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
        grade = await GradeRepository.get_by_lesson_and_student(db, data.lesson_id, data.student_id)

        if grade is None:
            grade = Grade(
                lesson_id=data.lesson_id,
                student_id=data.student_id,
                value=data.value,
                remark=data.remark,
            )
        else:
            grade.value = data.value
            grade.remark = data.remark

        res = await GradeRepository.upsert(db, grade)
        await db.commit()
        await db.refresh(res)
        return res

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
        lessons_res = await db.execute(
            select(Lesson.id).where(Lesson.journal_id == journal_id)
        )
        lesson_ids = [row[0] for row in lessons_res.fetchall()]

        return await GradeRepository.get_by_lesson_ids(db, lesson_ids)

    @staticmethod
    async def delete_grade(db: AsyncSession, journal_id: int, grade_id: int) -> None:
        grade = await GradeRepository.get_by_id_and_journal_id(db, grade_id, journal_id)
        if grade is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grade not found")

        await GradeRepository.delete(db, grade)
        await db.commit()


grade_service = GradeService()
