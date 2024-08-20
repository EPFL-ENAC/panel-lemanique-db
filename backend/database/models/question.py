from __future__ import annotations
from typing import Optional, TYPE_CHECKING, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .response import Response
    from .section import Section


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.id"))
    question_code: Mapped[str]
    question_text: Mapped[str]
    question_type: Mapped[Optional[str]]  # Optional for now, not in the future
    section: Mapped["Section"] = relationship(back_populates="questions")
    responses: Mapped[List["Response"]] = relationship(back_populates="question")
