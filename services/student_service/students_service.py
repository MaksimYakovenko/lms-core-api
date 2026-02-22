from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.student_model import Students
from models.group_model import Groups


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

    @staticmethod
    async def assign_student_to_group(db: AsyncSession, student_id: int, group_id: int):
        # Перевіряємо чи існує студент
        res = await db.execute(
            select(Students).where(Students.id == student_id))
        student = res.scalar_one_or_none()
        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        # Перевіряємо чи існує група
        group_res = await db.execute(
            select(Groups).where(Groups.id == group_id))
        group = group_res.scalar_one_or_none()
        if group is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Group not found"
            )

        # Прив'язуємо студента до групи
        student.group_id = group_id
        db.add(student)
        await db.commit()
        await db.refresh(student)
        return student


students_service = StudentService()
