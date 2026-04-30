from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.appointment_model import Appointments


class AppointmentRepository:
    @staticmethod
    async def get_appointments(db: AsyncSession) -> list[Appointments]:
        res = await db.execute(select(Appointments))
        appointments = res.scalars().all()
        return appointments
