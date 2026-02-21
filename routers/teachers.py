from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.teacher_model import Teachers
from schemas.teachers import TeacherCreateRequest, TeacherCreateResponse, \
    TeacherGetResponse
from services.teacher_service.teachers_service import teacher_service
from dependencies.require_roles import require_roles

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.post("/create_teacher", response_model=TeacherCreateResponse,
             dependencies=[Depends(require_roles("ADMIN"))])
async def create_teacher(payload: TeacherCreateRequest,
                         db: AsyncSession = Depends(get_db)):
    try:
        await teacher_service.create_teacher(
            db,
            email=payload.email,
            name="Unregistered",
            role=payload.role
        )
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Teacher is created"}
        )
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )

@router.get("/get_teachers", response_model=list[TeacherGetResponse],
            dependencies=[Depends(require_roles("ADMIN"))])
async def get_teachers(db: AsyncSession = Depends(get_db)):
    try:
        teachers = await teacher_service.get_teachers(db)
        return teachers
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )