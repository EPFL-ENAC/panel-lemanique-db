from sqlalchemy.orm import Session

from ..database.models.surveys import Surveys
from ..database.models.sections import Sections


def get_survey(db: Session, survey_id: int):
    return db.query(Surveys).filter(Surveys.survey_id == survey_id).first()


def get_surveys(db: Session, limit: int = 100):
    return db.query(Surveys).limit(limit).all()


def get_sections(db: Session, limit: int = 100):
    return db.query(Sections).limit(limit).all()
