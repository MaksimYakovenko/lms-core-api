from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.teacher_repository import TeacherRepository


class AppointmentService:
    @staticmethod
    async def get_appointments(db: AsyncSession):
        teachers = await TeacherRepository.get_all(db)
        for teacher in teachers:
            teacher.group_ids = [g.id for g in teacher.groups]
            teacher.subject_ids = [ts.subject_id for ts in teacher.teacher_subjects]
        return teachers


appointment_service = AppointmentService()
