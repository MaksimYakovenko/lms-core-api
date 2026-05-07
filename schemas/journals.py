from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import date
from schemas.grades import GradeResponse


class LessonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    date: date
    lesson_type: str
    order_index: int
    title: Optional[str] = None
    description: Optional[str] = None
    classroom_id: Optional[int] = None


class SubjectShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class TeacherShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class GroupShort(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
    journal_id: int
    id: int = Field(alias="group_id")
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


class JournalGroupedResponse(BaseModel):
    subject: str
    groups: List[GroupShort]


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
