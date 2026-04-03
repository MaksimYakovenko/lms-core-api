from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from dependencies.require_roles import require_roles
from schemas.lessons import LessonCreateRequest, LessonUpdateRequest, LessonResponse
from services.lesson_service.lesson_service import lesson_service

router = APIRouter(prefix="/journals/{journal_id}/lessons", tags=["Lessons"])


@router.post("", response_model=LessonResponse, status_code=status.HTTP_201_CREATED,
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
            topic=payload.topic,
        )
        return lesson
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("", response_model=list[LessonResponse],
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
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.put("/{lesson_id}", response_model=LessonResponse,
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
            topic=payload.topic,
        )
        return lesson
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.delete("/{lesson_id}", dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
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
