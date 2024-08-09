from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Participants(Base):
    __tablename__ = "participants"

    participant_code: Mapped[str] = mapped_column(primary_key=True)
    group: Mapped[int]
    gp_age_source: Mapped[Optional[int]]
    numero_insee: Mapped[Optional[int]]
    numero_ofs: Mapped[Optional[int]]
