from pydantic import BaseModel, ConfigDict
from typing import List


class AppointmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    group_ids: List[int] = []
    subject_ids: List[int] = []
