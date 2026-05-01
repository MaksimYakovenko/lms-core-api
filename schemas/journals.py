from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date
from schemas.grades import GradeResponse


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
    course_number: int


class StudentShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class JournalCreateRequest(BaseModel):
    group_id: int
    subject_id: int
    teacher_id: int
    assistant_id: Optional[int] = None


class JournalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    group: GroupShort
    subject: SubjectShort
    teacher: TeacherShort
    assistant: Optional[TeacherShort] = None


# class JournalListResponse(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#     id: int
#     group: GroupShort
#     subject: SubjectShort
#     teacher: TeacherShort
#     assistant: Optional[TeacherShort] = None
#     lessons: List[LessonResponse] = []


class JournalListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    subject: SubjectShort
    groups: List[GroupShort] = []


class JournalFullResponse(BaseModel):
    id: int
    group: GroupShort
    subject: SubjectShort
    teacher: TeacherShort
    assistant: Optional[TeacherShort] = None
    lessons: List[LessonResponse] = []
    students: List[StudentShort] = []
    grades: List[GradeResponse] = []

