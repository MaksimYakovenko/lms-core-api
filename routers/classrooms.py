from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.classroom_model import Classroom
from services.classroom_service.classroom_service import classroom_service
from dependencies.require_roles import require_roles
from schemas.classrooms import (
    ClassroomGetResponse,
    ClassroomCreateRequest,
    ClassroomCreateResponse
)

router = APIRouter(prefix="/classrooms", tags=["Classrooms"])


@router.get("/get_classrooms", response_model=list[ClassroomGetResponse])
async def get_classrooms(db: AsyncSession = Depends(get_db)):
    try:
        classrooms = await classroom_service.get_classrooms(db)
        return classrooms
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error {e}"
        )


@router.post("/create_classroom",
             dependencies=[Depends(require_roles("ADMIN"))],
             response_model=ClassroomCreateResponse)
async def create_classroom(payload: ClassroomCreateRequest,
                           db: AsyncSession = Depends(get_db)):
    try:
        await classroom_service.create_classroom(db, name=payload.name)
        return {"message": "Classroom created successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error {e}"
        )


@router.delete("/delete_classroom/{id}",
               dependencies=[Depends(require_roles("ADMIN"))])
async def delete_classroom(classroom_id: int,
                           db: AsyncSession = Depends(get_db)):
    try:
        await classroom_service.delete_classroom(db, classroom_id)
        return {"message": "Classroom is deleted"}
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.put("/update_classroom",
            dependencies=[Depends(require_roles("ADMIN"))],
            response_model=ClassroomGetResponse)
async def update_classroom(classroom_id: int, payload: ClassroomCreateRequest,
                           db: AsyncSession = Depends(get_db)):
    try:
        classroom = await classroom_service.update_classroom(db, classroom_id,
                                                             payload.name)
        return classroom
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error {e}"
        )
