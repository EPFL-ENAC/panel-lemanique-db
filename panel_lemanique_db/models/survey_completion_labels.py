from sqlalchemy import Column, Integer, Text
from .base import Base


class SurveyCompletionLabels(Base):
    __tablename__ = "survey_completion_labels"
    label_id = Column(Integer, primary_key=True)
    variable_name = Column(Text)
    value = Column(Integer)
    label = Column(Text)
