from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

class Subjects(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, index=True)
