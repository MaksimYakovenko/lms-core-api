from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional
from datetime import datetime


class StudentGetResponse(BaseModel):
    id: int
    email: EmailStr
    name: str = Field(min_length=2, max_length=100)
    role: str = Field(min_length=2, max_length=20)
    last_login: Optional[datetime] = None
