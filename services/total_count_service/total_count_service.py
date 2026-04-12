from sqlalchemy.ext.asyncio import AsyncSession
from repositories.total_count_repository import TotalCountRepository


class TotalCountService:
    @staticmethod
    async def get_total_teachers_count(db: AsyncSession) -> int:
        return await TotalCountRepository.get_total_teachers_count(db)

    @staticmethod
    async def get_total_students_count(db: AsyncSession) -> int:
        return await TotalCountRepository.get_total_students_count(db)

    @staticmethod
    async def get_total_groups_count(db: AsyncSession) -> int:
        return await TotalCountRepository.get_total_groups_count(db)

    @staticmethod
    async def get_total_subjects_count(db: AsyncSession) -> int:
        return await TotalCountRepository.get_total_subjects_count(db)


total_count_service = TotalCountService()
