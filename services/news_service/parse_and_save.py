from services.news_service.news_parser import NewsService
from models.news_model import News
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ParseAndSave:
    @staticmethod
    async def parse_and_save_news(db: AsyncSession) -> dict:
        news_data = await NewsService.fetch_news()

        saved_count = 0
        for news_item in news_data:
            existing = await db.execute(
                select(News).where(News.title == news_item["title"])
            )
            if existing.scalar_one_or_none() is None:
                new_news = News(
                    title=news_item["title"],
                    image_url=news_item["image_url"]
                )
                db.add(new_news)
                saved_count += 1

        await db.commit()

        return {
            "success": True,
            "total_parsed": len(news_data),
            "saved": saved_count,
            "skipped": len(news_data) - saved_count
        }
