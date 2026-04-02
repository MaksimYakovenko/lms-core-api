from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.teacher_model import Teachers
from schemas.teachers import (TeacherCreateRequest, TeacherCreateResponse, \
                              TeacherGetResponse, TeacherUpdateRequest,
                              TeacherDeleteResponse,
                              AssignTeacherToGroupsRequest,
                              AssignTeacherToGroupsResponse)
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
    except HTTPException:
        raise
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
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.put("/update_teacher/{id}",
            dependencies=[Depends(require_roles("ADMIN"))],
            response_model=TeacherGetResponse)
async def update_teacher(payload: TeacherUpdateRequest, db: AsyncSession =
Depends(get_db)):
    try:
        teacher = await teacher_service.update_teacher(db, payload.id,
                                                       payload.name)
        return teacher
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.put("/assign_to_groups",
            response_model=AssignTeacherToGroupsResponse,
            dependencies=[Depends(require_roles("ADMIN"))])
async def assign_student_to_group(
        request: AssignTeacherToGroupsRequest,
        db: AsyncSession = Depends(get_db)
):
    try:
        teacher = await teacher_service.assign_teacher_to_groups(
            db, request.teacher_id, request.group_ids
        )
        return teacher
    except HTTPException as e:
        raise e
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.delete("/delete_teacher/{id}", dependencies=[Depends(require_roles(
    "ADMIN"))], response_model=TeacherDeleteResponse)
async def delete_teacher(teacher_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await teacher_service.delete_teacher(db, teacher_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Teacher is deleted"}
        )
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )
