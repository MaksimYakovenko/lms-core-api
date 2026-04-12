from pydantic import BaseModel


class TotalCountGetResponse(BaseModel):
    total_teachers: int
    total_students: int
    total_groups: int
    total_subjects: int
