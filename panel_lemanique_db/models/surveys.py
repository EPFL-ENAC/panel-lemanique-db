from sqlalchemy import Column, Integer, Text, Date
from .base import Base


class Surveys(Base):
    __tablename__ = "surveys"
    survey_id = Column(Integer, primary_key=True)
    survey_topic = Column(Text)
    survey_date = Column(Date)
    survey_name = Column(Text)
