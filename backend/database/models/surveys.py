from datetime import date
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Surveys(Base):
    __tablename__ = "surveys"

    survey_id: Mapped[int] = mapped_column(primary_key=True)
    survey_topic: Mapped[str]
    survey_date: Mapped[date]
    survey_name: Mapped[str]
