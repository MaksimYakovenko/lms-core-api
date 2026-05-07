from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from dependencies.require_roles import require_roles
from schemas.lessons import LessonCreateRequest, LessonUpdateRequest, \
    LessonResponse
from services.lesson_service.lesson_service import lesson_service

router = APIRouter(tags=["Lessons"])


@router.get("/lessons/get_lesson_types",
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_lesson_types():
    try:
        lesson_types = await lesson_service.get_lesson_types()
        return lesson_types
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("/lessons/get_lesson_periods",
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_lesson_periods():
    try:
        lesson_periods = await lesson_service.get_lesson_periods()
        return lesson_periods
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.post("/journals/{journal_id}/lessons", response_model=LessonResponse,
             status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def add_lesson(
        journal_id: int,
        payload: LessonCreateRequest,
        db: AsyncSession = Depends(get_db)
):
    try:
        lesson = await lesson_service.add_lesson(
            db,
            journal_id=journal_id,
            lesson_date=payload.date,
            lesson_type=payload.lesson_type,
            classroom_id=payload.classroom_id,
            lesson_number=payload.lesson_number,
            lesson_title=payload.title,
            lesson_description=payload.description,
        )
        return lesson
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("/journals/{journal_id}/lessons",
            response_model=list[LessonResponse],
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_lessons(
        journal_id: int,
        db: AsyncSession = Depends(get_db)
):
    try:
        lessons = await lesson_service.get_lessons(db, journal_id)
        return lessons
    except HTTPException:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": f"Internal server error {e}"}
        )


@router.put("/journals/{journal_id}/lessons/{lesson_id}",
            response_model=LessonResponse,
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def update_lesson(
        journal_id: int,
        lesson_id: int,
        payload: LessonUpdateRequest,
        db: AsyncSession = Depends(get_db)
):
    try:
        lesson = await lesson_service.update_lesson(
            db,
            journal_id=journal_id,
            lesson_id=lesson_id,
            lesson_date=payload.date,
            lesson_type=payload.lesson_type,
            classroom_id=payload.classroom_id,
            lesson_number=payload.lesson_number,
            lesson_title=payload.title,
            lesson_description=payload.description,
        )
        return lesson
    except HTTPException:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": f"Internal server error {e}"}
        )


@router.delete("/journals/{journal_id}/lessons/{lesson_id}",
               dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def delete_lesson(
        journal_id: int,
        lesson_id: int,
        db: AsyncSession = Depends(get_db)
):
    try:
        await lesson_service.delete_lesson(db, journal_id, lesson_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Lesson deleted"}
        )
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )
