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


class UsersBlockRequest(BaseModel):
    users: list[EmailStr] = Field(
        ...,
        examples=[["user1@example.com", "user2@example.com"]]
    )


class UsersBlockResponse(BaseModel):
    success: bool = Field()
    message: str = Field()
    blocked_count: int = Field()
    already_blocked: list[str] = Field(default_factory=list, )
    not_found: list[str] = Field(default_factory=list, )


class UsersUnblockRequest(BaseModel):
    users: list[EmailStr] = Field(
        examples=[["user1@example.com", "user2@example.com"]]
    )


class UsersUnblockResponse(BaseModel):
    success: bool = Field()
    message: str = Field()
    unblocked_count: int = Field()
    already_active: list[str] = Field(default_factory=list)
    not_found: list[str] = Field(default_factory=list,)
