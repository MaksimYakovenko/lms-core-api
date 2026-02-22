from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.teacher_model import Teachers


class TeacherService:
    @staticmethod
    async def create_teacher(db: AsyncSession,
                             *,
                             email: str,
                             name: str,
                             role: str,
                             ) -> Teachers:
        res = await db.execute(select(Teachers).where(Teachers.email == email))
        if res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Teacher already existed"
            )

        teacher = Teachers(
            email=email,
            name=name,
            role=role
        )

        db.add(teacher)
        await db.commit()
        await db.refresh(teacher)
        return teacher

    @staticmethod
    async def get_teachers(db: AsyncSession) -> list[Teachers]:
        res = await db.execute(select(Teachers))
        teachers = res.scalars().all()
        return teachers

    @staticmethod
    async def delete_teacher(db: AsyncSession, teacher_id: int):
        res = await db.execute(
            select(Teachers).where(Teachers.id == teacher_id))
        teacher = res.scalar_one_or_none()
        if teacher is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found"
            )

        await db.delete(teacher)
        await db.commit()

    @staticmethod
    async def update_teacher(db: AsyncSession, teacher_id: int, name: str):
        res = await db.execute(
            select(Teachers).where(Teachers.id == teacher_id))
        teacher = res.scalar_one_or_none()
        if teacher is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found"
            )

        teacher.name = name
        db.add(teacher)
        await db.commit()
        await db.refresh(teacher)
        return teacher


teacher_service = TeacherService()
