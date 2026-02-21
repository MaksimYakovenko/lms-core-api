from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.news_model import News
from services.news_service.news_parser import NewsService

router = APIRouter(prefix="/news", tags=["News"])


@router.get("")
async def get_news_list(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(News))
    return res.scalars().all()

@router.get("/parse/titles")
async def parse_titles():
    try:
        parser = NewsService()
        titles = await parser.fetch_titles()
        return {
            "success": True,
            "count": len(titles),
            "titles": titles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
