from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date


class LessonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    date: date
    lesson_type: str
    order_index: int
    topic: Optional[str] = None


class SubjectShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class TeacherShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class GroupShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class StudentShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


# ── Journal schemas ─────────────────────────────────────────────
class JournalCreateRequest(BaseModel):
    group_id: int
    subject_id: int
    teacher_id: int
    assistant_id: Optional[int] = None


class JournalResponse(BaseModel):
    """Відповідь після створення журналу"""
    model_config = ConfigDict(from_attributes=True)
    id: int
    group: GroupShort
    subject: SubjectShort
    teacher: TeacherShort
    assistant: Optional[TeacherShort] = None


class JournalListResponse(BaseModel):
    """Список журналів (без студентів — для перегляду списку)"""
    model_config = ConfigDict(from_attributes=True)
    id: int
    group: GroupShort
    subject: SubjectShort
    teacher: TeacherShort
    assistant: Optional[TeacherShort] = None
    lessons: List[LessonResponse] = []


class JournalFullResponse(BaseModel):
    """Повний журнал з уроками та студентами групи"""
    id: int
    group: GroupShort
    subject: SubjectShort
    teacher: TeacherShort
    assistant: Optional[TeacherShort] = None
    lessons: List[LessonResponse] = []
    students: List[StudentShort] = []   # автоматично з групи

