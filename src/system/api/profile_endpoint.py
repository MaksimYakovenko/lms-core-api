from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from src.system.auth import get_current_authenticated_user

router = APIRouter()

@router.get('/profile')
async def get_profile(current_user: dict[str, object] = Depends(get_current_authenticated_user)) -> dict[str, object]:
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")


    profile = {"id": current_user["id"], "username": current_user["username"], "email": current_user["email"]}

    return {"profile": profile, "status": "success"}
