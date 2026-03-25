from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.student_model import Students
from models.group_model import Groups
from models.auth_model import User


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

        user_res = await db.execute(
            select(User).where(User.email == student.email))
        user = user_res.scalar_one_or_none()
        if user is not None:
            await db.delete(user)

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

        user_res = await db.execute(
            select(User).where(User.email == student.email))
        user = user_res.scalar_one_or_none()
        if user is not None:
            parts = name.split(" ", 1)
            user.first_name = parts[0]
            user.last_name = parts[1] if len(parts) > 1 else ""
            db.add(user)

        await db.commit()
        await db.refresh(student)
        return student

    @staticmethod
    async def assign_student_to_group(db: AsyncSession, student_id: int,
                                      group_id: int):
        res = await db.execute(
            select(Students).where(Students.id == student_id))
        student = res.scalar_one_or_none()
        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        group_res = await db.execute(
            select(Groups).where(Groups.id == group_id))
        group = group_res.scalar_one_or_none()
        if group is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Group not found"
            )

        student.group_id = group_id
        db.add(student)
        await db.commit()
        await db.refresh(student)
        return student


students_service = StudentService()
