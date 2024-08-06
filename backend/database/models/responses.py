from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Responses(Base):
    __tablename__ = "responses"

    response_id: Mapped[int] = mapped_column(primary_key=True)
    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.participant_id")
    )
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.question_id"))
    response_text: Mapped[str]
    response_value: Mapped[int]
