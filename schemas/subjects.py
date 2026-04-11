from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Literal, Optional
from datetime import datetime


class SubjectGetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str = Field(min_length=2, max_length=150)


class SubjectCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=150)


class SubjectUpdateRequest(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=150)
