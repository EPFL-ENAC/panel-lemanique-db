from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Sections(Base):
    __tablename__ = "sections"

    section_id: Mapped[int] = mapped_column(primary_key=True)
    section_topic: Mapped[Optional[str]]
    section_name: Mapped[str]
    survey_id: Mapped[int] = mapped_column(ForeignKey("surveys.survey_id"))
