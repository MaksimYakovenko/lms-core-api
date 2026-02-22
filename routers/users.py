from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.news_model import News
from dependencies.current_user import get_current_user
from schemas.users import (
    UserResponse,
    UsersBlockRequest,
    UsersBlockResponse,
    UsersUnblockRequest,
    UsersUnblockResponse
)
from models.auth_model import User
from dependencies.require_roles import require_roles
from services.user_service.user_block_service import users_block_service
from services.user_service.users_unblock_service import users_unblock_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
        current_user: User = Depends(get_current_user)
):
    return current_user


@router.post("/block", response_model=UsersBlockResponse,
             dependencies=[Depends(require_roles("ADMIN"))])
async def block_users(
        request: UsersBlockRequest,
        db: AsyncSession = Depends(get_db)
):
    try:
        result = await users_block_service.block_users(db, request.users)
        return result
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/unblock", response_model=UsersUnblockResponse,
             dependencies=[Depends(require_roles("ADMIN"))])
async def unblock_users(
        request: UsersUnblockRequest,
        db: AsyncSession = Depends(get_db)
):
    try:
        result = await users_unblock_service.unblock_users(db, request.users)
        return result
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
