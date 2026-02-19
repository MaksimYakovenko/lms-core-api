from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional
from datetime import datetime


class TeacherCreateRequest(BaseModel):
    email: EmailStr
    role: Literal["TEACHER"] = "TEACHER"


class TeacherCreateResponse(BaseModel):
    message: str


class TeacherGetResponse(BaseModel):
    email: EmailStr
    name: str = Field("Unregistered", min_length=2, max_length=100)
    role: str = Field(min_length=2, max_length=20)
    last_login: Optional[datetime] = None
