from __future__ import annotations

from fastapi import HTTPException

def validate_profile_access(requesting_user_id: int, target_user_id: int) -> None:
    """Validate access to user profile based on authentication."""
    if requesting_user_id != target_user_id:
        raise HTTPException(status_code=403, detail="Access denied.")
