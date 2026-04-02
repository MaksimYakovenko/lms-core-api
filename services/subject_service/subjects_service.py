from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.subject_model import Subjects


class SubjectService:
    @staticmethod
    async def get_subjects(db: AsyncSession) -> list[Subjects]:
        res = await db.execute(select(Subjects))
        subjects = res.scalars().all()
        return subjects

    @staticmethod
    async def create_subject(db: AsyncSession, name: str):
        existing_subject = await db.execute(
            select(Subjects).where(Subjects.name == name))
        if existing_subject.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Subject with this name already exists"
            )

        new_subject = Subjects(name=name)
        db.add(new_subject)
        await db.commit()
        await db.refresh(new_subject)
        return new_subject

    @staticmethod
    async def delete_subject(db: AsyncSession, subject_id: int):
        res = await db.execute(
            select(Subjects).where(Subjects.id == subject_id))
        subject = res.scalar_one_or_none()
        if subject is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subject not found"
            )

        await db.delete(subject)
        await db.commit()

    @staticmethod
    async def update_subject(db: AsyncSession, subject_id: int, name: str):
        res = await db.execute(
            select(Subjects).where(Subjects.id == subject_id))
        subject = res.scalar_one_or_none()
        if subject is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subject not found"
            )

        existing_subject = await db.execute(
            select(Subjects).where(Subjects.name == name))
        if existing_subject.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Subject with this name already exists"
            )

        subject.name = name
        db.add(subject)
        await db.commit()
        await db.refresh(subject)
        return subject


subjects_service = SubjectService()
