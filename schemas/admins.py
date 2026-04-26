from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Literal, Optional
from datetime import datetime

class AdminCreateRequest(BaseModel):
    email: EmailStr
    role: Literal["ADMIN"] = "ADMIN"


class AdminCreateResponse(BaseModel):
    message: str


class AdminGetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str = Field("Unregistered", min_length=2, max_length=100)
    role: str = Field(min_length=2, max_length=20)
    status: str = Field("INVITED", min_length=2, max_length=20)
    last_login: Optional[datetime] = None


class AdminUpdateRequest(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=100)


class AdminUpdateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str
    role: str
    last_login: Optional[datetime] = None

