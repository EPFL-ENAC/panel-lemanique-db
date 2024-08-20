from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class SurveyCompletionLabel(Base):
    __tablename__ = "survey_completion_labels"

    label_id: Mapped[int] = mapped_column(primary_key=True)
    variable_name: Mapped[str]
    value: Mapped[int]
    label: Mapped[str]
