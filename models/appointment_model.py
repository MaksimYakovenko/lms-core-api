from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from db import Base


class Appointments(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    teacher_name = Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    teacher_groups = Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    teacher_subjects = Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
