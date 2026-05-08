from fastapi import HTTPException, status
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.teacher_model import Teachers
from models.admin_model import Admins
from models.auth_model import User
from models.group_model import Groups
from models.subject_model import Subjects
from models.teacher_subject import TeacherSubject
from repositories.teacher_repository import TeacherRepository


class TeacherService:
    @staticmethod
    async def create_teacher(db: AsyncSession,
                             *,
                             email: str,
                             name: str,
                             role: str,
                             user_status: str = "INVITED"
                             ) -> Teachers:
        admin_res = await db.execute(
            select(Admins).where(Admins.email == email))
        if admin_res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists as an admin"
            )

        existing_teacher = await TeacherRepository.get_by_email(db, email)
        if existing_teacher:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Teacher already existed"
            )

        teacher = Teachers(
            email=email,
            name=name,
            role=role,
            status=user_status
        )

        res = await TeacherRepository.create(db, teacher)
        await db.commit()
        await db.refresh(res)
        return res

    @staticmethod
    async def get_teachers(db: AsyncSession) -> list[Teachers]:
        teachers = await TeacherRepository.get_all(db)
        for teacher in teachers:
            teacher.group_ids = [g.id for g in teacher.groups]
            teacher.subject_ids = [ts.subject_id for ts in teacher.teacher_subjects]
        return teachers

    @staticmethod
    async def delete_teacher(db: AsyncSession, teacher_id: int):
        teacher = await TeacherRepository.get_by_id(db, teacher_id)
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

        await TeacherRepository.delete(db, teacher)
        await db.commit()

    @staticmethod
    async def update_teacher(db: AsyncSession, teacher_id: int, name: str):
        teacher = await TeacherRepository.get_by_id(db, teacher_id)
        if teacher is None:
            raise HTTPException(

                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found"
            )

        teacher.name = name
        await TeacherRepository.update(db, teacher)

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
        teacher.subject_ids = [ts.subject_id for ts in teacher.teacher_subjects]
        return teacher

    @staticmethod
    async def assign_teacher_to_groups(db: AsyncSession, teacher_id: int,
                                       group_ids: list[int]):
        teacher = await TeacherRepository.get_by_id(db, teacher_id)
        if teacher is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found"
            )

        group_ids = list(dict.fromkeys(group_ids))

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
        await TeacherRepository.update(db, teacher)
        await db.commit()
        await db.refresh(teacher)
        teacher.group_ids = [g.id for g in teacher.groups]
        teacher.subject_ids = [ts.subject_id for ts in teacher.teacher_subjects]
        return teacher

    @staticmethod
    async def assign_teacher_to_subjects(db: AsyncSession, teacher_id: int,
                                       subject_ids: list[int]):
        teacher = await TeacherRepository.get_by_id(db, teacher_id)
        if teacher is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found"
            )

        subject_ids = list(dict.fromkeys(subject_ids))  # deduplicate, preserve order

        subjects_res = await db.execute(
            select(Subjects).where(Subjects.id.in_(subject_ids)))
        subjects = subjects_res.scalars().all()

        if len(subjects) != len(subject_ids):
            found_ids = {s.id for s in subjects}
            missing = [sid for sid in subject_ids if sid not in found_ids]
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Subjects not found: {missing}"
            )

        await db.execute(
            delete(TeacherSubject).where(TeacherSubject.teacher_id == teacher_id)
        )
        await db.flush()

        for subject_id in subject_ids:
            teacher_subject = TeacherSubject(
                teacher_id=teacher_id,
                subject_id=subject_id
            )
            db.add(teacher_subject)

        await db.commit()
        await db.refresh(teacher)
        teacher.subject_ids = [ts.subject_id for ts in teacher.teacher_subjects]
        return teacher

    # @staticmethod
    # async def get_teacher_subjects(db: AsyncSession, teacher_id: int) -> list[Subjects]:
    #     teacher = await TeacherRepository.get_by_id(db, teacher_id)
    #     if teacher is None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    #
    #     ts_res = await db.execute(
    #         select(TeacherSubject).where(TeacherSubject.teacher_id == teacher_id)
    #     )
    #     teacher_subjects = ts_res.scalars().all()
    #     subject_ids = [ts.subject_id for ts in teacher_subjects]
    #
    #     if not subject_ids:
    #         return []
    #
    #     subjects_res = await db.execute(select(Subjects).where(Subjects.id.in_(subject_ids)))
    #     return subjects_res.scalars().all()


teacher_service = TeacherService()
