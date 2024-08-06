from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class ParticipantLabels(Base):
    __tablename__ = "participant_labels"

    label_id: Mapped[int] = mapped_column(primary_key=True)
    variable_name: Mapped[str]
    value: Mapped[int]
    label: Mapped[str]
