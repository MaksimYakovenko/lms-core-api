import httpx
from bs4 import BeautifulSoup
from core.constants import BASE_URL, HEADERS


class NewsService:
    @staticmethod
    async def fetch_news() -> list[dict]:

        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
                response = await client.get(BASE_URL, headers=HEADERS,
                                            timeout=10.0)
                response.raise_for_status()
            except Exception as e:
                print(f"Error fetching news: {e}")
                return []

        soup = BeautifulSoup(response.text, 'html.parser')
        news_list = []

        img_tags = soup.find_all('img')

        for img in img_tags:
            title = img.get('alt', '').strip()
            image_url = img.get('src', '').strip()
            if not title or not image_url:
                continue

            if image_url.startswith('/'):
                image_url = f"{BASE_URL}{image_url}"
            elif not image_url.startswith('http'):
                image_url = f"{BASE_URL}/{image_url}"

            news_list.append({
                "title": title,
                "image_url": image_url
            })

        return news_list
