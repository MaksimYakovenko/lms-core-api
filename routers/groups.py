from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from services.group_service.group_service import group_service
from dependencies.require_roles import require_roles
from db.database import get_db
from schemas.groups import GroupCreateRequest


router = APIRouter(prefix="/groups", tags=["Groups"])


@router.get("/get_groups")
async def get_groups(db: AsyncSession = Depends(get_db)):
    try:
        groups = await group_service.get_groups(db)
        return groups
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


@router.post("/create_group")
async def create_group(payload: GroupCreateRequest, db: AsyncSession = Depends(get_db)):
    try:
        await group_service.create_group(db, payload.name, payload.course_number)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Group created"}
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
