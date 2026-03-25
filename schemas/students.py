from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Literal, Optional
from datetime import datetime


class StudentGetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str = Field(min_length=2, max_length=100)
    role: str = Field(min_length=2, max_length=20)
    group_id: Optional[int] = None
    last_login: Optional[datetime] = None


class StudentCreateRequest(BaseModel):
    email: EmailStr
    role: Literal["STUDENT"] = "STUDENT"


class StudentCreateResponse(BaseModel):
    message: str


class AssignStudentToGroupRequest(BaseModel):
    student_id: int
    group_id: int


class AssignStudentToGroupResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str
    group_id: Optional[int] = None


class StudentUpdateRequest(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=100)


class StudentUpdateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str
    role: str
    group_id: Optional[int] = None
    last_login: Optional[datetime] = None

