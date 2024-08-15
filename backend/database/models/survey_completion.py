from typing import Optional, TYPE_CHECKING
from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .participants import Participants
    from .surveys import Surveys


class SurveyCompletion(Base):
    __tablename__ = "survey_completion"

    completion_id: Mapped[int] = mapped_column(primary_key=True)
    participant_code: Mapped[str] = mapped_column(
        ForeignKey("participants.participant_code")
    )
    survey_id: Mapped[int] = mapped_column(ForeignKey("surveys.survey_id"))
    count_miss1: Mapped[Optional[int]]
    count_miss2: Mapped[Optional[int]]
    progress: Mapped[Optional[int]]
    start_date: Mapped[Optional[date]]
    end_date: Mapped[Optional[date]]
    temps_minute: Mapped[Optional[float]]
    participant: Mapped["Participants"] = relationship(
        "Participants", back_populates="survey_completions"
    )
    survey: Mapped["Surveys"] = relationship(
        "Surveys", back_populates="survey_completions"
    )
