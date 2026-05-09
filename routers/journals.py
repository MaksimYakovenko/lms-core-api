from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.responses import JSONResponse, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from db.database import get_db
from dependencies.require_roles import require_roles
from dependencies.current_user import get_current_user
from models.auth_model import User
from models.teacher_model import Teachers
from schemas.journals import JournalCreateRequest, JournalResponse, \
    JournalListResponse, JournalFullResponse, JournalGroupedResponse
from services.journal_service.journal_service import journal_service

router = APIRouter(prefix="/journals", tags=["Journals"])


@router.get("/my", response_model=list[JournalGroupedResponse],
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_my_journals(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    try:
        teacher_res = await db.execute(select(Teachers).where(Teachers.email == current_user.email))
        teacher = teacher_res.scalar_one_or_none()
        if teacher is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
        journals = await journal_service.get_my_journals(db, teacher.id)
        return journals
    except HTTPException:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": f"Internal server error {e}"}
        )


@router.post("", response_model=JournalResponse,
             status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def create_journal(
        payload: JournalCreateRequest,
        db: AsyncSession = Depends(get_db)
):
    try:
        journal = await journal_service.create_journal(
            db,
            group_id=payload.group_id,
            subject_id=payload.subject_id,
            teacher_id=payload.teacher_id,
            assistant_id=payload.assistant_id,
        )
        return journal
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("", response_model=list[JournalGroupedResponse],
            dependencies=[Depends(require_roles("ADMIN"))])
async def get_journals(
        db: AsyncSession = Depends(get_db)
):
    try:
        journals = await journal_service.get_journals(db)
        return journals
    except HTTPException:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": f"Internal server error {e}"}
        )


@router.get("/{journal_id}", response_model=JournalFullResponse,
            dependencies=[Depends(require_roles("ADMIN", "TEACHER"))])
async def get_journal(
        journal_id: int,
        db: AsyncSession = Depends(get_db)
):
    try:
        journal = await journal_service.get_journal_by_id(db, journal_id)
        return journal
    except HTTPException:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": f"Internal server error {e}"}
        )


@router.delete("/{journal_id}", dependencies=[Depends(require_roles("ADMIN"))])
async def delete_journal(
        journal_id: int,
        db: AsyncSession = Depends(get_db)
):
    try:
        await journal_service.delete_journal(db, journal_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Journal deleted"}
        )
    except HTTPException:
        raise
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"}
        )


@router.get("/{journal_id}/export")
async def export_journal(journal_id: int, db: AsyncSession = Depends(get_db)):
    data = await journal_service.export_journal_to_excel(db, journal_id)
    return Response(
        content=data,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": f"attachment; filename=journal_{journal_id}.xlsx"}
    )
