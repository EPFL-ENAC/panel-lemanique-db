from typing import Optional
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Surveys(Base):
    __tablename__ = "surveys"

    survey_id: Mapped[int] = mapped_column(primary_key=True)
    survey_topic: Mapped[Optional[str]]
    survey_date: Mapped[Optional[date]]
    survey_name: Mapped[Optional[str]]
