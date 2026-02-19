from pydantic import BaseModel, Field, EmailStr


class TeacherCreateRequest(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    role: str = Field(min_length=2, max_length=20)


class TeacherCreateResponse(BaseModel):
    message: str


class TeacherGetResponse(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    role: str = Field(min_length=2, max_length=20)