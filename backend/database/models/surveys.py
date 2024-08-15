from typing import Optional, TYPE_CHECKING
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .sections import Sections
    from .survey_completion import SurveyCompletion


class Surveys(Base):
    __tablename__ = "surveys"

    survey_id: Mapped[int] = mapped_column(primary_key=True)
    survey_topic: Mapped[Optional[str]]
    survey_date: Mapped[Optional[date]]
    survey_name: Mapped[Optional[str]]
    sections: Mapped["Sections"] = relationship("Sections", back_populates="survey")
    survey_completions: Mapped["SurveyCompletion"] = relationship(
        "SurveyCompletion", back_populates="survey"
    )
