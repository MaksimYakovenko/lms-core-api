from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.journal_model import Journal
from models.teacher_model import Teachers
from models.group_model import Groups
from models.subject_model import Subjects
from models.teacher_subject import TeacherSubject


class JournalService:

    @staticmethod
    async def create_journal(
        db: AsyncSession,
        group_id: int,
        subject_id: int,
        teacher_id: int,
        assistant_id: int | None = None,
    ) -> Journal:
        # Перевірка групи
        group = await db.get(Groups, group_id)
        if group is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")

        # Перевірка предмету
        subject = await db.get(Subjects, subject_id)
        if subject is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")

        # Перевірка вчителя
        teacher = await db.get(Teachers, teacher_id)
        if teacher is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")

        # Перевірка що вчитель може викладати цей предмет
        ts_res = await db.execute(
            select(TeacherSubject).where(
                TeacherSubject.teacher_id == teacher_id,
                TeacherSubject.subject_id == subject_id,
            )
        )
        if ts_res.scalar_one_or_none() is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Teacher is not assigned to this subject",
            )

        # Перевірка асистента
        if assistant_id is not None:
            assistant = await db.get(Teachers, assistant_id)
            if assistant is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assistant not found")

        # Перевірка унікальності журналу (група + предмет)
        existing = await db.execute(
            select(Journal).where(
                Journal.group_id == group_id,
                Journal.subject_id == subject_id,
            )
        )
        if existing.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Journal for this group and subject already exists",
            )

        journal = Journal(
            group_id=group_id,
            subject_id=subject_id,
            teacher_id=teacher_id,
            assistant_id=assistant_id,
        )
        db.add(journal)
        await db.commit()
        await db.refresh(journal)
        return journal

    @staticmethod
    async def get_journals(
        db: AsyncSession,
        group_id: int | None = None,
        teacher_id: int | None = None,
    ) -> list[Journal]:
        query = select(Journal)
        if group_id is not None:
            query = query.where(Journal.group_id == group_id)
        if teacher_id is not None:
            query = query.where(Journal.teacher_id == teacher_id)
        res = await db.execute(query)
        return res.scalars().all()

    @staticmethod
    async def get_journal_by_id(db: AsyncSession, journal_id: int) -> Journal:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal not found")
        return journal

    @staticmethod
    async def delete_journal(db: AsyncSession, journal_id: int) -> None:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal not found")
        await db.delete(journal)
        await db.commit()


journal_service = JournalService()
