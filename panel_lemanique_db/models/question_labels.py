from sqlalchemy import Column, Integer, Text
from .base import Base


class QuestionLabels(Base):
    __tablename__ = "question_labels"
    label_id = Column(Integer, primary_key=True)
    variable_name = Column(Text)
    value = Column(Integer)
    label = Column(Text)
