from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date
from core.constants import LessonType


class LessonCreateRequest(BaseModel):
    date: date
    lesson_type: LessonType = LessonType.LESSON
    topic: Optional[str] = None


class LessonUpdateRequest(BaseModel):
    date: Optional[date] = None
    lesson_type: Optional[LessonType] = None
    topic: Optional[str] = None


class LessonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    journal_id: int
    date: date
    lesson_type: str
    order_index: int
    topic: Optional[str] = None
