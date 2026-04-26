from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Literal, Optional, List
from datetime import datetime


class TeacherCreateRequest(BaseModel):
    email: EmailStr
    role: Literal["TEACHER"] = "TEACHER"


class TeacherCreateResponse(BaseModel):
    message: str


class TeacherGetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    name: str = Field("Unregistered", min_length=2, max_length=100)
    role: str = Field(min_length=2, max_length=20)
    user_status: str = Field("INVITED", min_length=2, max_length=20)
    last_login: Optional[datetime] = None
    group_ids: List[int] = []


class TeacherDeleteResponse(BaseModel):
    message: str


class TeacherUpdateRequest(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=100)


class AssignTeacherToGroupsRequest(BaseModel):
    teacher_id: int
    group_ids: list[int]


class AssignTeacherToGroupsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    name: str
    role: str
    last_login: Optional[datetime] = None
    group_ids: List[int] = []


class AssignSubjectToTeacherRequest(BaseModel):
    subject_id: int


class TeacherSubjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class TeacherSubjectsListResponse(BaseModel):
    teacher_id: int
    subjects: List[TeacherSubjectResponse]
