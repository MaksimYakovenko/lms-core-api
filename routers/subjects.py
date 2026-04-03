from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from services.subject_service.subjects_service import subjects_service
from dependencies.require_roles import require_roles
from dependencies.current_user import get_current_user
from schemas.subjects import SubjectGetResponse, SubjectCreateRequest
from db.database import get_db
from models.auth_model import User

router = APIRouter(prefix="/subjects", tags=["Subjects"])


@router.get("/my", response_model=list[SubjectGetResponse],
            dependencies=[Depends(require_roles("TEACHER"))])
async def get_my_subjects(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    """Предмети які може викладати поточний вчитель (для дропдауну при створенні журналу)"""
    try:
        subjects = await subjects_service.get_my_subjects(db, current_user.email)
        return subjects
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("/get_subjects", response_model=list[SubjectGetResponse],
            dependencies=[Depends(require_roles("ADMIN"))])
async def get_students(db: AsyncSession = Depends(get_db)):
    try:
        subjects = await subjects_service.get_subjects(db)
        return subjects
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.post("/create_subject", response_model=SubjectGetResponse,
             dependencies=[Depends(require_roles("ADMIN"))])
async def create_subject(payload: SubjectCreateRequest,
                         db: AsyncSession = Depends(get_db)):
    try:
        subject = await subjects_service.create_subject(db, payload.name)
        return subject
    except HTTPException as e:
        raise e
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.put("/update_subject/{id}",
            dependencies=[Depends(require_roles("ADMIN"))],
            response_model=SubjectGetResponse)
async def update_subject(subject_id: int, payload: SubjectCreateRequest,
                         db: AsyncSession = Depends(get_db)):
    try:
        subject = await subjects_service.update_subject(db, subject_id,
                                                        payload.name)
        return subject
    except HTTPException as e:
        raise e
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.delete("/delete_subject/{id}",
               dependencies=[Depends(require_roles("ADMIN"))])
async def delete_subject(subject_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await subjects_service.delete_subject(db, subject_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Subject is deleted"}
        )
    except HTTPException as e:
        raise e
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )
