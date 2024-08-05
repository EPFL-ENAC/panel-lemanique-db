from sqlalchemy import Column, Date, Float, Integer, ForeignKey
from .base import Base


class SurveyCompletion(Base):
    __tablename__ = "survey_completion"
    participant_id = Column(Integer, ForeignKey("participants.participant_id"))
    survey_id = Column(Integer, ForeignKey("surveys.survey_id"))
    count_miss1 = Column(Integer)
    count_miss2 = Column(Integer)
    progress = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    temps_minute = Column(Float)
