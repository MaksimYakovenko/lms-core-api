from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from datetime import date
from db.database import Base
from core.constants import LessonType


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    journal_id: Mapped[int] = mapped_column(Integer, ForeignKey("journals.id", ondelete="CASCADE"), nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    lesson_type: Mapped[str] = mapped_column(String(10), nullable=False,
                                             default=LessonType.LECTURE)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    lesson_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    classroom_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("classrooms.id", ondelete="SET NULL"), nullable=True)
    topic: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    journal = relationship("Journal", back_populates="lessons")
    grades: Mapped[list["Grade"]] = relationship(
        "Grade", back_populates="lesson", lazy="selectin",
        cascade="all, delete-orphan"
    )
