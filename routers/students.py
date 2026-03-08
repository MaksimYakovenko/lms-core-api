from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from sqlalchemy.future import select
from schemas.students import StudentGetResponse, AssignStudentToGroupRequest, AssignStudentToGroupResponse
from services.student_service.students_service import students_service
from dependencies.require_roles import require_roles
from db.database import get_db

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/get_students", response_model=list[StudentGetResponse],
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_students(db: AsyncSession = Depends(get_db)):
    try:
        students = await students_service.get_students(db)
        return students
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.delete("/delete_student/{id}",
               dependencies=[Depends(require_roles("ADMIN"))])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await students_service.delete_student(db, student_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Student is deleted"}
        )
    except HTTPException as e:
        raise e
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )

@router.put("/update_student/{id}",
            dependencies=[Depends(require_roles("ADMIN"))],
            response_model=StudentGetResponse)
async def update_student(student_id: int, name: str, db: AsyncSession = Depends(get_db)):
    try:
        student = await students_service.update_student(db, student_id, name)
        return student
    except HTTPException as e:
        raise e
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.put("/assign_to_group",
            dependencies=[Depends(require_roles("ADMIN"))],
            response_model=AssignStudentToGroupResponse)
async def assign_student_to_group(
    request: AssignStudentToGroupRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        student = await students_service.assign_student_to_group(
            db, request.student_id, request.group_id
        )
        return student
    except HTTPException as e:
        raise e
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )

