from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.classroom_model import Classroom
from fastapi import HTTPException, status
from repositories.classroom_repository import ClassroomRepository
from repositories.student_repository import StudentRepository


class ClassroomService:
    @staticmethod
    async def get_classrooms(db: AsyncSession) -> list[Classroom]:
        return await ClassroomRepository.get_all(db)

    @staticmethod
    async def delete_classroom(db: AsyncSession, classroom_id: int):
        classroom = await ClassroomRepository.get_by_id(db, classroom_id)
        if classroom is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Classroom not found"
            )

        await ClassroomRepository.delete(db, classroom)
        await db.commit()

    @staticmethod
    async def create_classroom(db: AsyncSession,
                               *,
                               name: str,
                               ) -> Classroom:
        classroom_res = await db.execute(
            select(Classroom).where(Classroom.name == name))
        if classroom_res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Classroom already exists"
            )

        classroom = Classroom(name=name)

        res = await ClassroomRepository.create(db, classroom)
        await db.commit()
        await db.refresh(res)
        return res

    @staticmethod
    async def update_classroom(db: AsyncSession, classroom_id: int, name: str):
        classroom = await ClassroomRepository.get_by_id(db, classroom_id)
        if classroom is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Classroom not found"
            )

        classroom.name = name
        await ClassroomRepository.update(db, classroom)

        await db.commit()
        await db.refresh(classroom)
        return classroom


classroom_service = ClassroomService()
