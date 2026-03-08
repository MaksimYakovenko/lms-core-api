from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional
from datetime import datetime


class StudentGetResponse(BaseModel):
    id: int
    email: EmailStr
    name: str = Field(min_length=2, max_length=100)
    role: str = Field(min_length=2, max_length=20)
    group_id: Optional[int] = None
    last_login: Optional[datetime] = None


class AssignStudentToGroupRequest(BaseModel):
    student_id: int
    group_id: int


class AssignStudentToGroupResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    group_id: Optional[int] = None


