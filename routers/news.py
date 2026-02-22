from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.database import get_db
from models.news_model import News
from services.news_service.parse_and_save import ParseAndSave
from dependencies.require_roles import require_roles
from schemas.news import NewsResponse, NewsParseResponse

router = APIRouter(prefix="/news", tags=["News"])


@router.get("", dependencies=[Depends(require_roles("ADMIN", "TEACHER",
                                                    "STUDENT"))],
            response_model=list[NewsResponse])
async def get_news_list(db: AsyncSession = Depends(get_db)):
    try:
        res = await db.execute(select(News))
        return res.scalars().all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}", dependencies=[
    Depends(require_roles("ADMIN", "TEACHER", "STUDENT"))],
            response_model=NewsResponse)
async def get_news_item(news_id: int, db: AsyncSession = Depends(get_db)):
    try:
        res = await db.execute(select(News).where(News.id == news_id))
        news_item = res.scalar_one_or_none()
        if news_item is None:
            raise HTTPException(status_code=404, detail="News item not found")
        return news_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/parse/save", dependencies=[Depends(require_roles("ADMIN"))],
             response_model=NewsParseResponse)
async def parse_and_save_news(db: AsyncSession = Depends(get_db)):
    try:
        result = await ParseAndSave.parse_and_save_news(db)
        return result
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
