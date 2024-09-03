from __future__ import annotations
from typing import Optional, TYPE_CHECKING, List
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base


if TYPE_CHECKING:
    from .response import Response
    from .survey_completion import SurveyCompletion


class Participant(Base):
    __tablename__ = "participants"

    participant_code: Mapped[str] = mapped_column(primary_key=True)
    group: Mapped[int]
    gp_age_source: Mapped[Optional[int]]
    numero_insee: Mapped[Optional[int]]
    numero_ofs: Mapped[Optional[int]]
    responses: Mapped[List["Response"]] = relationship(back_populates="participant")
    survey_completions: Mapped[List["SurveyCompletion"]] = relationship(
        back_populates="participant"
    )
