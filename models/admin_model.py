from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Optional
from db.database import Base


class Admins(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    role: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(20), server_default="ACTIVE")
    last_login: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True)
