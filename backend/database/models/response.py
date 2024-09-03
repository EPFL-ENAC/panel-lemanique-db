from typing import Optional, TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .participant import Participant
    from .question import Question


class Response(Base):
    __tablename__ = "responses"

    id: Mapped[int] = mapped_column(primary_key=True)
    participant_code: Mapped[str] = mapped_column(
        ForeignKey("participants.participant_code")
    )
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    response_text: Mapped[Optional[str]]
    response_value: Mapped[Optional[int]]
    question: Mapped["Question"] = relationship(back_populates="responses")
    participant: Mapped["Participant"] = relationship(back_populates="responses")
