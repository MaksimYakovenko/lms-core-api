from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.student_model import Students


class StudentService:
    @staticmethod
    async def get_students(db: AsyncSession) -> list[Students]:
        res = await db.execute(select(Students))
        students = res.scalars().all()
        return students

    @staticmethod
    async def delete_student(db: AsyncSession, student_id: int):
        res = await db.execute(
            select(Students).where(Students.id == student_id))
        student = res.scalar_one_or_none()
        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        await db.delete(student)
        await db.commit()

    @staticmethod
    async def update_student(db: AsyncSession, student_id: int, name: str):
        res = await db.execute(
            select(Students).where(Students.id == student_id))
        student = res.scalar_one_or_none()
        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        student.name = name
        db.add(student)
        await db.commit()
        await db.refresh(student)
        return student


students_service = StudentService()
