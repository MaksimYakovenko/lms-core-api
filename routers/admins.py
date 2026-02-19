from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.admins import AdminCreateRequest, AdminGetResponse, \
    AdminCreateResponse
from services.admin_service.admins_service import admin_service
from dependencies.require_roles import require_roles

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post("/create_admin", response_model=AdminCreateResponse,
             dependencies=[Depends(require_roles("ADMIN"))])
async def create_admin(payload: AdminCreateRequest,
                       db: AsyncSession = Depends(get_db)):
    await admin_service.create_admin(
        db,
        email=payload.email,
        name="Unregistered",
        role=payload.role
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Admin is created"}
    )


@router.get("/get_admins", response_model=list[AdminGetResponse],
            dependencies=[Depends(require_roles("ADMIN"))])
async def get_admins(db: AsyncSession = Depends(get_db)):
    admins = await admin_service.get_admins(db)
    return admins
