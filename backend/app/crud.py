from sqlalchemy.orm import Session

from ..database.models.surveys import Surveys


def get_survey(db: Session, survey_id: int):
    return db.query(Surveys).filter(Surveys.survey_id == survey_id).first()
