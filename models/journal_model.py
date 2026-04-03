from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from db.database import Base


class Journal(Base):
    __tablename__ = "journals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False)
    assistant_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"), nullable=True)

    __table_args__ = (
        UniqueConstraint("group_id", "subject_id", name="uq_journal_group_subject"),
    )

    group = relationship("Groups", foreign_keys=[group_id], lazy="selectin")
    subject = relationship("Subjects", foreign_keys=[subject_id], lazy="selectin")
    teacher = relationship("Teachers", foreign_keys=[teacher_id], lazy="selectin")
    assistant = relationship("Teachers", foreign_keys=[assistant_id], lazy="selectin")
    lessons: Mapped[List["Lesson"]] = relationship(
        "Lesson", back_populates="journal", lazy="selectin",
        cascade="all, delete-orphan", order_by="Lesson.order_index"
    )
