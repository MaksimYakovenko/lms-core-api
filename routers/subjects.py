from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from services.group_service.group_service import group_service
from dependencies.require_roles import require_roles
from db.database import get_db

router = APIRouter(prefix="/subjects", tags=["Subjects"])
