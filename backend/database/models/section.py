from __future__ import annotations
from typing import Optional, TYPE_CHECKING, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .survey import Survey
    from .question import Question


class Section(Base):
    __tablename__ = "sections"

    id: Mapped[int] = mapped_column(primary_key=True)
    section_topic: Mapped[Optional[str]]
    section_name: Mapped[str]
    survey_id: Mapped[int] = mapped_column(ForeignKey("surveys.id"))
    survey: Mapped["Survey"] = relationship(back_populates="sections")
    questions: Mapped[List["Question"]] = relationship(back_populates="section")
