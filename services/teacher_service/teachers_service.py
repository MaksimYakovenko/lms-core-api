from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.teacher_model import Teachers


class TeacherService:
    @staticmethod
    async def create_teacher(db: AsyncSession,
                             *,
                             email: str,
                             first_name: str,
                             last_name: str,
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
            first_name=first_name,
            last_name=last_name,
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

teacher_service = TeacherService()
