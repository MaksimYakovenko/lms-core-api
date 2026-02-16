from pydantic import BaseModel, EmailStr, Field, field_validator
import re

_name_pattern = re.compile(r"^[A-Za-z'-]+$")
_password_pattern = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,16}$"
)


class SignUpIn(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=8, max_length=64)


class SignUpRequest(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    password: str = Field(min_length=8, max_length=64)

    @field_validator("first_name", "last_name")
    def validate_name(cls, value):
        if value is None:
            return value
        if not _name_pattern.match(value):
            raise ValueError(
                "Only Latin letters, hyphens, and apostrophes are accepted in string"
            )
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if value is None:
            return value
        if not _password_pattern.match(value):
            raise ValueError(
                "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"
            )
        return value


class SignUpResponse(BaseModel):
    message: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
