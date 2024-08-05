from sqlalchemy import Column, Integer, Text, ForeignKey
from .base import Base


class Questions(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey("sections.section_id"))
    question_code = Column(Text)
    question_text = Column(Text)
    question_type = Column(Text)
