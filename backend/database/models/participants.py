from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .responses import Responses
    from .survey_completion import SurveyCompletion


class Participants(Base):
    __tablename__ = "participants"

    participant_code: Mapped[str] = mapped_column(primary_key=True)
    group: Mapped[int]
    gp_age_source: Mapped[Optional[int]]
    numero_insee: Mapped[Optional[int]]
    numero_ofs: Mapped[Optional[int]]
    responses: Mapped["Responses"] = relationship(back_populates="participant")
    survey_completions: Mapped["SurveyCompletion"] = relationship(
        back_populates="participant"
    )
