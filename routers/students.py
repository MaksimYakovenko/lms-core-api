from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from schemas.students import StudentGetResponse
from services.student_service.students_service import students_service
from dependencies.require_roles import require_roles

from db.database import get_db

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/get_students", response_model=list[StudentGetResponse],
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_students(db: AsyncSession = Depends(get_db)):
    students = await students_service.get_students(db)
    return students
