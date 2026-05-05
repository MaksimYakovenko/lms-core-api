from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date as Date
from core.constants import LessonType


class LessonCreateRequest(BaseModel):
    date: Date
    lesson_type: LessonType = LessonType.LECTURE
    classroom_id: Optional[int] = None
    lesson_number: Optional[int] = None


class LessonUpdateRequest(BaseModel):
    date: Optional[Date] = None
    lesson_type: Optional[LessonType] = None
    classroom_id: Optional[int] = None
    lesson_number: Optional[int] = None


class LessonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    journal_id: int
    date: Date
    lesson_type: str
    order_index: int
    lesson_number: Optional[int] = None
    classroom_id: Optional[int] = None
