from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from models.admin_model import Admins
from models.teacher_model import Teachers
from models.auth_model import User
from datetime import datetime, timezone


async def extract_role(db: AsyncSession,
                       *,
                       email: str,
                       first_name: str,
                       last_name: str) -> str:
    teacher_res = await db.execute(
        select(Teachers).where(Teachers.email == email))
    teacher = teacher_res.scalar_one_or_none()

    admin_res = await db.execute(
        select(Admins).where(Admins.email == email))
    admin = admin_res.scalar_one_or_none()

    role = "STUDENT"
    full_name = f"{first_name} {last_name}"

    if teacher:
        role = "TEACHER"
        await db.execute(
            update(Teachers)
            .where(Teachers.email == email)
            .values(name=full_name)
        )
    elif admin:
        role = "ADMIN"
        await db.execute(
            update(Admins)
            .where(Admins.email == email)
            .values(name=full_name)
        )

    return role


async def update_last_login(db: AsyncSession, user: User) -> None:
    current_time = datetime.now(timezone.utc)
    user.last_login = current_time

    if user.role == "TEACHER":
        await db.execute(
            update(Teachers)
            .where(Teachers.email == user.email)
            .values(last_login=current_time)
        )
    elif user.role == "ADMIN":
        await db.execute(
            update(Admins)
            .where(Admins.email == user.email)
            .values(last_login=current_time)
        )
