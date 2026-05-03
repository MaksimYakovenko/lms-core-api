from pydantic import BaseModel, Field, ConfigDict


class ClassroomGetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str = Field(min_length=2, max_length=100)


class ClassroomCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)


class ClassroomCreateResponse(BaseModel):
    message: str
