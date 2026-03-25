from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.admins import AdminCreateRequest, AdminGetResponse, \
    AdminCreateResponse, AdminUpdateRequest, AdminUpdateResponse
from services.admin_service.admins_service import admin_service
from dependencies.require_roles import require_roles

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post("/create_admin", response_model=AdminCreateResponse,
             )
async def create_admin(payload: AdminCreateRequest,
                       db: AsyncSession = Depends(get_db)):
    try:
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
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("/get_admins", response_model=list[AdminGetResponse],
            dependencies=[Depends(require_roles("ADMIN"))])
async def get_admins(db: AsyncSession = Depends(get_db)):
    try:
        admins = await admin_service.get_admins(db)
        return admins
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.put("/update_admin",
            dependencies=[Depends(require_roles("ADMIN"))],
            response_model=AdminUpdateResponse)
async def update_admin(payload: AdminUpdateRequest, db: AsyncSession =
Depends(get_db)):
    try:
        admin = await admin_service.update_admin(db, payload.id, payload.name)
        return admin
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.delete("/delete_admin/{id}",
               dependencies=[Depends(require_roles("ADMIN"))])
async def delete_admin(admin_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await admin_service.delete_admin(db, admin_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Admin is deleted"}
        )
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )
