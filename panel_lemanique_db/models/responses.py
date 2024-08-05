from sqlalchemy import Column, Integer, Text, ForeignKey
from .base import Base


class Responses(Base):
    __tablename__ = "responses"
    participant_id = Column(Integer, ForeignKey("participants.participant_id"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    response_text = Column(Text)
    response_value = Column(Integer)
