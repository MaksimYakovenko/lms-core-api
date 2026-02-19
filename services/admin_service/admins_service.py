from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.admin_model import Admins


class AdminService:
    @staticmethod
    async def create_admin(db: AsyncSession,
                           *,
                           email: str,
                           first_name: str,
                           last_name: str,
                           role: str,
                           ) -> Admins:
        res = await db.execute(select(Admins).where(Admins.email == email))
        if res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Admin already existed"
            )

        admin = Admins(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role
        )

        db.add(admin)
        await db.commit()
        await db.refresh(admin)
        return admin

    @staticmethod
    async def get_admins(db: AsyncSession) -> list[Admins]:
        res = await db.execute(select(Admins))
        admins = res.scalars().all()
        return admins


admin_service = AdminService()
