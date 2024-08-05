from sqlalchemy import Column, Integer
from .base import Base


class Participants(Base):
    __tablename__ = "participants"
    participant_id = Column(Integer, primary_key=True)
    group = Column(Integer)
    gp_age_source = Column(Integer)
    numero_insee = Column(Integer)
    numero_ofs = Column(Integer)
