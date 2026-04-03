from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.teacher_model import Teachers
from models.admin_model import Admins
from models.auth_model import User
from models.group_model import Groups
from models.subject_model import Subjects
from models.teacher_subject import TeacherSubject


class TeacherService:
    @staticmethod
    async def create_teacher(db: AsyncSession,
                             *,
                             email: str,
                             name: str,
                             role: str,
                             ) -> Teachers:
        admin_res = await db.execute(
            select(Admins).where(Admins.email == email))
        if admin_res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists as an admin"
            )

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
        for teacher in teachers:
            teacher.group_ids = [g.id for g in teacher.groups]
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

        user_res = await db.execute(
            select(User).where(User.email == teacher.email))
        user = user_res.scalar_one_or_none()
        if user is not None:
            await db.delete(user)

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

        user_res = await db.execute(
            select(User).where(User.email == teacher.email))
        user = user_res.scalar_one_or_none()
        if user is not None:
            parts = name.split(" ", 1)
            user.first_name = parts[0]
            user.last_name = parts[1] if len(parts) > 1 else ""
            db.add(user)

        await db.commit()
        await db.refresh(teacher)
        teacher.group_ids = [g.id for g in teacher.groups]
        return teacher

    @staticmethod
    async def assign_teacher_to_groups(db: AsyncSession, teacher_id: int,
                                       group_ids: list[int]):
        res = await db.execute(
            select(Teachers).where(Teachers.id == teacher_id))
        teacher = res.scalar_one_or_none()
        if teacher is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found"
            )

        groups_res = await db.execute(
            select(Groups).where(Groups.id.in_(group_ids)))
        groups = groups_res.scalars().all()

        if len(groups) != len(group_ids):
            found_ids = {g.id for g in groups}
            missing = [gid for gid in group_ids if gid not in found_ids]
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Groups not found: {missing}"
            )

        teacher.groups = list(groups)
        db.add(teacher)
        await db.commit()
        await db.refresh(teacher)
        teacher.group_ids = [g.id for g in teacher.groups]
        return teacher

    @staticmethod
    async def assign_subject_to_teacher(db: AsyncSession, teacher_id: int, subject_id: int):
        teacher_res = await db.execute(select(Teachers).where(Teachers.id == teacher_id))
        teacher = teacher_res.scalar_one_or_none()
        if teacher is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")

        subject_res = await db.execute(select(Subjects).where(Subjects.id == subject_id))
        subject = subject_res.scalar_one_or_none()
        if subject is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")

        existing = await db.execute(
            select(TeacherSubject).where(
                TeacherSubject.teacher_id == teacher_id,
                TeacherSubject.subject_id == subject_id
            )
        )
        if existing.scalar_one_or_none() is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Subject already assigned to this teacher")

        ts = TeacherSubject(teacher_id=teacher_id, subject_id=subject_id)
        db.add(ts)
        await db.commit()

    @staticmethod
    async def remove_subject_from_teacher(db: AsyncSession, teacher_id: int, subject_id: int):
        teacher_res = await db.execute(select(Teachers).where(Teachers.id == teacher_id))
        if teacher_res.scalar_one_or_none() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")

        ts_res = await db.execute(
            select(TeacherSubject).where(
                TeacherSubject.teacher_id == teacher_id,
                TeacherSubject.subject_id == subject_id
            )
        )
        ts = ts_res.scalar_one_or_none()
        if ts is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not assigned to this teacher")

        await db.delete(ts)
        await db.commit()

    @staticmethod
    async def get_teacher_subjects(db: AsyncSession, teacher_id: int) -> list[Subjects]:
        teacher_res = await db.execute(select(Teachers).where(Teachers.id == teacher_id))
        teacher = teacher_res.scalar_one_or_none()
        if teacher is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")

        ts_res = await db.execute(
            select(TeacherSubject).where(TeacherSubject.teacher_id == teacher_id)
        )
        teacher_subjects = ts_res.scalars().all()
        subject_ids = [ts.subject_id for ts in teacher_subjects]

        if not subject_ids:
            return []

        subjects_res = await db.execute(select(Subjects).where(Subjects.id.in_(subject_ids)))
        return subjects_res.scalars().all()


teacher_service = TeacherService()
