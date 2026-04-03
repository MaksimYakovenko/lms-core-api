from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class GradeUpsertRequest(BaseModel):
    lesson_id: int
    student_id: int
    value: Optional[str] = None   # "8", "11", "П", "Н/О", "С" тощо
    remark: Optional[str] = None


class GradeBulkUpsertRequest(BaseModel):
    grades: List[GradeUpsertRequest]


class GradeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    lesson_id: int
    student_id: int
    value: Optional[str] = None
    remark: Optional[str] = None
