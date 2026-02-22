from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.auth_model import User
from models.student_model import Students
from models.admin_model import Admins
from models.teacher_model import Teachers


class UserBlockService:
    @staticmethod
    async def block_users(db: AsyncSession, emails: list[str]) -> dict:
        if not emails:
            return {
                "success": False,
                "message": "The list of users is empty",
                "blocked_count": 0,
                "not_found": []
            }

        models = [User, Students, Admins, Teachers]

        blocked_count = 0
        already_blocked = []
        found_emails = set()

        for model in models:
            result = await db.execute(
                select(model).where(model.email.in_(emails))
            )
            users = result.scalars().all()

            for user in users:
                found_emails.add(user.email)
                if user.status == "ACTIVE":
                    user.status = "BLOCKED"
                    blocked_count += 1
                else:
                    if user.email not in already_blocked:
                        already_blocked.append(user.email)

        not_found_emails = [email for email in emails if
                            email not in found_emails]

        await db.commit()

        return {
            "success": True,
            "message": f"Blocked {blocked_count} users",
            "blocked_count": blocked_count,
            "already_blocked": already_blocked,
            "not_found": not_found_emails
        }


users_block_service = UserBlockService()
