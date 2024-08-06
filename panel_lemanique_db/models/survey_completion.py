from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class SurveyCompletion(Base):
    __tablename__ = "survey_completion"

    completion_id: Mapped[int] = mapped_column(primary_key=True)
    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.participant_id")
    )
    survey_id: Mapped[int] = mapped_column(ForeignKey("surveys.survey_id"))
    count_miss1: Mapped[int]
    count_miss2: Mapped[int]
    progress: Mapped[int]
    start_date: Mapped[date]
    end_date: Mapped[date]
    temps_minute: Mapped[float]
