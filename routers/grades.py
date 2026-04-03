from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from dependencies.require_roles import require_roles
from schemas.grades import GradeUpsertRequest, GradeBulkUpsertRequest, GradeResponse
from services.grade_service.grade_service import grade_service

router = APIRouter(prefix="/journals/{journal_id}/grades", tags=["Grades"])


@router.put("", response_model=GradeResponse,
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def upsert_grade(
        journal_id: int,
        payload: GradeUpsertRequest,
        db: AsyncSession = Depends(get_db)
):
    """Виставити або оновити одну оцінку (upsert)"""
    try:
        grade = await grade_service.upsert_grade(db, journal_id, payload)
        return grade
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.put("/bulk", response_model=list[GradeResponse],
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def bulk_upsert_grades(
        journal_id: int,
        payload: GradeBulkUpsertRequest,
        db: AsyncSession = Depends(get_db)
):
    """Масове виставлення оцінок"""
    try:
        grades = await grade_service.bulk_upsert_grades(db, journal_id, payload.grades)
        return grades
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("", response_model=list[GradeResponse],
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_grades(
        journal_id: int,
        db: AsyncSession = Depends(get_db)
):
    """Отримати всі оцінки журналу"""
    try:
        grades = await grade_service.get_grades(db, journal_id)
        return grades
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.delete("/{grade_id}",
               dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def delete_grade(
        journal_id: int,
        grade_id: int,
        db: AsyncSession = Depends(get_db)
):
    """Очистити оцінку"""
    try:
        await grade_service.delete_grade(db, journal_id, grade_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Grade deleted"}
        )
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )
