from sqlalchemy import Column, Integer, Text, ForeignKey
from .base import Base


class Sections(Base):
    __tablename__ = "sections"
    section_id = Column(Integer, primary_key=True)
    section_topic = Column(Text)
    section_name = Column(Text)
    survey_id = Column(Integer, ForeignKey("surveys.survey_id"))
