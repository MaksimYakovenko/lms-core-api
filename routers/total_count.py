from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from dependencies.require_roles import require_roles
from services.total_count_service.total_count_service import total_count_service
from schemas.total_count import TotalCountGetResponse

router = APIRouter(prefix="/total_count", tags=["Total Count"])


@router.get("", dependencies=[Depends(require_roles("ADMIN"))],
            response_model=TotalCountGetResponse)
async def get_total_count(db: AsyncSession = Depends(get_db)):
    try:
        total_teachers = await total_count_service.get_total_teachers_count(db)
        total_students = await total_count_service.get_total_students_count(db)
        total_groups = await total_count_service.get_total_groups_count(db)
        total_subjects = await total_count_service.get_total_subjects_count(db)
        return TotalCountGetResponse(
            total_teachers=total_teachers,
            total_students=total_students,
            total_groups=total_groups,
            total_subjects=total_subjects
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
