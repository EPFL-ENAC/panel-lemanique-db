from typing import Optional, TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .participants import Participants
    from .questions import Questions


class Responses(Base):
    __tablename__ = "responses"

    response_id: Mapped[int] = mapped_column(primary_key=True)
    participant_code: Mapped[str] = mapped_column(
        ForeignKey("participants.participant_code")
    )
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.question_id"))
    response_text: Mapped[Optional[str]]
    response_value: Mapped[Optional[int]]
    participant: Mapped["Participants"] = relationship(back_populates="responses")
    question: Mapped["Questions"] = relationship(back_populates="responses")
