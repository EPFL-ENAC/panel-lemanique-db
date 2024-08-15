from typing import Optional, TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

if TYPE_CHECKING:
    from .surveys import Surveys


class Sections(Base):
    __tablename__ = "sections"

    section_id: Mapped[int] = mapped_column(primary_key=True)
    section_topic: Mapped[Optional[str]]
    section_name: Mapped[str]
    survey_id: Mapped[int] = mapped_column(ForeignKey("surveys.survey_id"))
    survey: Mapped["Surveys"] = relationship(back_populates="sections")
