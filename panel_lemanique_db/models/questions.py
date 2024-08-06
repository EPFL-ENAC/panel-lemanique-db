from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Questions(Base):
    __tablename__ = "questions"

    question_id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.section_id"))
    question_code: Mapped[str]
    question_text: Mapped[str]
    question_type: Mapped[str]
