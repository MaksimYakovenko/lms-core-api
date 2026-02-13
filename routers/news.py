from fastapi import APIRouter

router = APIRouter(prefix="/news", tags=["News"])


@router.get("")
async def health_check():
    return {
        "status": "unhealthy",
        "service": "lms-core-api"
    }
