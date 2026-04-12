from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text


class TotalCountRepository:
    @staticmethod
    async def get_total_teachers_count(db: AsyncSession) -> int:
        res = await db.execute(text("SELECT COUNT(*) FROM teachers WHERE name <> 'Unregistered'"))
        return res.scalar_one()

    @staticmethod
    async def get_total_students_count(db: AsyncSession) -> int:
        res = await db.execute(text("SELECT COUNT(*) FROM students WHERE name <> 'Unregistered'"))
        return res.scalar_one()

    @staticmethod
    async def get_total_groups_count(db: AsyncSession) -> int:
        res = await db.execute(text("SELECT COUNT(*) FROM groups"))
        return res.scalar_one()

    @staticmethod
    async def get_total_subjects_count(db: AsyncSession) -> int:
        res = await db.execute(text("SELECT COUNT(*) FROM subjects"))
        return res.scalar_one()
