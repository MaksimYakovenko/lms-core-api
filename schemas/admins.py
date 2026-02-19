from pydantic import BaseModel, Field, EmailStr
from typing import Literal

class AdminCreateRequest(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    role: Literal["ADMIN"] = "ADMIN"


class AdminCreateResponse(BaseModel):
    message: str


class AdminGetResponse(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    role: str = Field(min_length=2, max_length=20)