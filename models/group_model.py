from sqlalchemy import CheckConstraint
from db.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Groups(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    course_number: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("course_number >= 1 AND course_number <= 6"),
    )