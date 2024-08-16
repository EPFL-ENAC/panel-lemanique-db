from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .participant import Participant
    from .survey import Survey


class SurveyCompletion(Base):
    __tablename__ = "survey_completion"

    id: Mapped[int] = mapped_column(primary_key=True)
    participant_code: Mapped[str] = mapped_column(
        ForeignKey("participants.participant_code")
    )
    survey_id: Mapped[int] = mapped_column(ForeignKey("surveys.id"))
    count_miss1: Mapped[Optional[int]]
    count_miss2: Mapped[Optional[int]]
    progress: Mapped[Optional[int]]
    start_date: Mapped[Optional[date]]
    end_date: Mapped[Optional[date]]
    temps_minute: Mapped[Optional[float]]
    participant: Mapped["Participant"] = relationship(
        back_populates="survey_completions"
    )
    survey: Mapped["Survey"] = relationship(back_populates="survey_completions")
