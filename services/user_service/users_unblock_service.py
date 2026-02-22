from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.auth_model import User
from models.student_model import Students
from models.admin_model import Admins
from models.teacher_model import Teachers


class UserUnblockService:
    @staticmethod
    async def unblock_users(db: AsyncSession, emails: list[str]) -> dict:
        if not emails:
            return {
                "success": False,
                "message": "The list of users is empty",
                "unblocked_count": 0,
                "not_found": []
            }

        models = [User, Students, Admins, Teachers]

        unblocked_count = 0
        already_active = []
        found_emails = set()

        for model in models:
            result = await db.execute(
                select(model).where(model.email.in_(emails))
            )
            users = result.scalars().all()

            for user in users:
                found_emails.add(user.email)
                if user.status == "BLOCKED":
                    user.status = "ACTIVE"
                    unblocked_count += 1
                else:
                    if user.email not in already_active:
                        already_active.append(user.email)

        not_found_emails = [email for email in emails if
                            email not in found_emails]

        await db.commit()

        return {
            "success": True,
            "message": f"Unblocked {unblocked_count} users",
            "unblocked_count": unblocked_count,
            "already_active": already_active,
            "not_found": not_found_emails
        }


users_unblock_service = UserUnblockService()
