from pydantic import BaseModel


class GroupCreateRequest(BaseModel):
    name: str
    course_number: int
