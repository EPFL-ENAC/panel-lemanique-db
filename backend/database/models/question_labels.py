from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class QuestionLabels(Base):
    __tablename__ = "question_labels"

    label_id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.question_id"))
    value: Mapped[int]
    label: Mapped[str]
