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


students_service = StudentService()
