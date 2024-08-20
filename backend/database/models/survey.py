from __future__ import annotations
from typing import Optional, TYPE_CHECKING, List
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .section import Section
    from .survey_completion import SurveyCompletion


class Survey(Base):
    __tablename__ = "surveys"

    id: Mapped[int] = mapped_column(primary_key=True)
    survey_topic: Mapped[Optional[str]]
    survey_date: Mapped[Optional[date]]
    survey_name: Mapped[Optional[str]]
    sections: Mapped[List["Section"]] = relationship(back_populates="survey")
    survey_completions: Mapped[List["SurveyCompletion"]] = relationship(
        back_populates="survey"
    )
