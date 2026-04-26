from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.admin_model import Admins
from models.teacher_model import Teachers
from models.auth_model import User
from repositories.admin_repository import AdminRepository


class AdminService:
    @staticmethod
    async def create_admin(db: AsyncSession,
                           *,
                           email: str,
                           name: str,
                           role: str,
                           ) -> Admins:
        teacher_res = await db.execute(select(Teachers).where(Teachers.email == email))
        if teacher_res.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists as a teacher"
            )

        existing_admin = await AdminRepository.get_by_email(db, email)
        if existing_admin:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Admin already existed"
            )

        admin = Admins(
            email=email,
            name=name,
            role=role,
            status="INVITED"
        )

        res = await AdminRepository.create(db, admin)
        await db.commit()
        await db.refresh(res)
        return res

    @staticmethod
    async def get_admins(db: AsyncSession) -> list[Admins]:
        return await AdminRepository.get_all(db)

    @staticmethod
    async def delete_admin(db: AsyncSession, admin_id: int):
        admin = await AdminRepository.get_by_id(db, admin_id)
        if admin is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Admin not found"
            )

        user_res = await db.execute(
            select(User).where(User.email == admin.email))
        user = user_res.scalar_one_or_none()
        if user is not None:
            await db.delete(user)

        await AdminRepository.delete(db, admin)
        await db.commit()

    @staticmethod
    async def update_admin(db: AsyncSession, admin_id: int, name: str):
        admin = await AdminRepository.get_by_id(db, admin_id)
        if admin is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Admin not found"
            )

        admin.name = name
        await AdminRepository.update(db, admin)

        user_res = await db.execute(
            select(User).where(User.email == admin.email))
        user = user_res.scalar_one_or_none()
        if user is not None:
            parts = name.split(" ", 1)
            user.first_name = parts[0]
            user.last_name = parts[1] if len(parts) > 1 else ""
            db.add(user)

        await db.commit()
        await db.refresh(admin)
        return admin


admin_service = AdminService()
