from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    role: Literal["ADMIN", "TEACHER", "STUDENT"] = Field(default="STUDENT")
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True
