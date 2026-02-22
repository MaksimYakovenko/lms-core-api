from pydantic import BaseModel


class NewsResponse(BaseModel):
    id: int
    title: str
    image_url: str | None

class NewsParseResponse(BaseModel):
    success: bool
    total_parsed: int
    saved: int
    skipped: int