from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.news_model import News

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/sign-in")
async def get_news_list(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(News))
    return res.scalars().all()

@router.get("/sign-up", status_code=201)
async def sign_up():
    return {
        "status": "unhealthy",
        "service": "lms-core-api"
    }
