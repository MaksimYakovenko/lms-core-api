import httpx
from bs4 import BeautifulSoup
from typing import List
from core.constants import BASE_URL, HEADERS


class NewsService:
    @staticmethod
    async def fetch_titles_with_details() -> List[dict]:
        try:
            async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
                response = await client.get(BASE_URL, headers=HEADERS)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'lxml')
                titles = soup.find_all('h5', class_='lp-box-title')

                result = []
                for idx, title in enumerate(titles):
                    result.append({
                        'index': idx + 1,
                        'title': title.get_text(strip=True),
                        'html': str(title)
                    })

                return result

        except httpx.HTTPError as e:
            raise Exception(f"Error requesting the site {str(e)}")
        except Exception as e:
            raise Exception(f"Parsing error {str(e)}")

news_service = NewsService()