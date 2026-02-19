from pydantic import BaseModel, Field, EmailStr


class AdminCreateRequest(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    role: str = Field(min_length=2, max_length=20)


class AdminCreateResponse(BaseModel):
    message: str


class AdminGetResponse(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    role: str = Field(min_length=2, max_length=20)