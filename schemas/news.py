from pydantic import BaseModel


class NewsResponse(BaseModel):
    id: int
    title: str
    image_url: str | None