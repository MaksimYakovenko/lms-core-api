from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.appointments import AppointmentResponse
from services.appointment_service.appointment_service import appointment_service
from dependencies.require_roles import require_roles

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.get("/get_appointments", response_model=list[AppointmentResponse],
            dependencies=[Depends(require_roles("ADMIN"))])
async def get_appointments(db: AsyncSession = Depends(get_db)):
    try:
        appointments = await appointment_service.get_appointments(db)
        return appointments
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )
