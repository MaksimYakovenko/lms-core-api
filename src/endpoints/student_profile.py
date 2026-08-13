from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from some_jwt_library import decode_jwt
from db_service import get_student_profile

# Define API Router for student profile endpoint
router = APIRouter()

@router.get("/student/profile")
async def student_profile(request: Request) -> JSONResponse:
    """
    Retrieve the student profile based on an authenticated JWT token.

    Parameters:
        request (Request): The incoming request containing headers.

    Returns:
        JSONResponse: The JSON response with the student profile or error.
    """
    try:
        # Extract JWT from Authorization header
        auth_header = request.headers.get("Authorization")
        if auth_header is None or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid or missing JWT token.")

        jwt_token = auth_header.split(" ")[1]
        # Decode and validate JWT
        try:
            user_info = decode_jwt(jwt_token)
        except Exception as err:
            raise HTTPException(status_code=401, detail="Invalid JWT token.")

        if "student_id" not in user_info:
            raise HTTPException(status_code=403, detail="Invalid authentication token.")

        student_id = user_info["student_id"]

        # Retrieve profile from student profile service
        try:
            profile = await get_student_profile(student_id)
        except Exception as err:
            raise HTTPException(status_code=404, detail="Student profile not found.")

        return JSONResponse(content={"profile": profile})

    except HTTPException as err:
        raise err
    except Exception as error:
        raise HTTPException(status_code=500, detail="Unexpected server error.") from error
