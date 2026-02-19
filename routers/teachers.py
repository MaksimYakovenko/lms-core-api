from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.teacher_model import Teachers
from schemas.teachers import TeacherCreateRequest, TeacherCreateResponse, \
    TeacherGetResponse
from services.teacher_service.teachers_service import teacher_service

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.post("/create_teacher", response_model=TeacherCreateResponse)
async def create_teacher(payload: TeacherCreateRequest,
                         db: AsyncSession = Depends(get_db)):
    await teacher_service.create_teacher(
        db,
        email=payload.email,
        first_name=payload.first_name,
        last_name=payload.last_name,
        role=payload.role
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Teacher is created"}
    )


@router.get("/get_teachers", response_model=list[TeacherGetResponse])
async def get_teachers(db: AsyncSession = Depends(get_db)):
    teachers = await teacher_service.get_teachers(db)
    return teachers
