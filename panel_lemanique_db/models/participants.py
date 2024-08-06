from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Participants(Base):
    __tablename__ = "participants"

    participant_id: Mapped[int] = mapped_column(primary_key=True)
    group: Mapped[int]
    gp_age_source: Mapped[int]
    numero_insee: Mapped[int]
    numero_ofs: Mapped[int]
