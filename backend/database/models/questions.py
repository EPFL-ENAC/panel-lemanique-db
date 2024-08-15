from typing import Optional, TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .responses import Responses


class Questions(Base):
    __tablename__ = "questions"

    question_id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.section_id"))
    question_code: Mapped[str]
    question_text: Mapped[str]
    question_type: Mapped[Optional[str]]  # Optional for now, not in the future
    responses: Mapped["Responses"] = relationship(back_populates="question")
