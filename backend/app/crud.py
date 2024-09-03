from sqlalchemy.orm import Session
from sqlalchemy import Select, text
from typing import List
from ..database.models.survey import Survey
from ..database.models.section import Section
from ..database.models.participant import Participant
from ..database.models.response import Response
from ..database.models.survey_completion import SurveyCompletion  # noqa F401
from ..database.models.question import Question
from .schemas import CrosstableResult


def get_survey(db: Session, survey_id: int):
    statement = Select(Survey).where(Survey.id == survey_id)
    results = db.execute(statement).scalars().first()
    return results.__dict__


def get_surveys(db: Session, limit: int = 100):
    statement = Select(Survey).limit(limit)
    results = db.execute(statement).scalars().all()
    return [survey.__dict__ for survey in results]


def get_sections(db: Session, limit: int = 100):
    statement = Select(Section).limit(limit)
    results = db.execute(statement).scalars().all()
    return [section.__dict__ for section in results]


def get_participant(db: Session, participant_code: str):
    statement = Select(Participant).where(
        Participant.participant_code == participant_code
    )
    results = db.execute(statement).scalars().first()
    return results.__dict__


def get_responses_for_participant(db: Session, participant_code: str, limit: int = 10):
    # import pdb; pdb.set_trace()
    statement = (
        Select(Response)
        .where(Response.participant_code == participant_code)
        .limit(limit)
    )
    results = db.execute(statement).scalars().all()
    return [response.__dict__ for response in results]


def get_questions(db: Session, limit: int = 100):
    statement = Select(Question).limit(limit)
    results = db.execute(statement).scalars().all()
    return [section.__dict__ for section in results]


def get_responses(db: Session, limit: int = 100):
    return db.query(Response).limit(limit).all()


def get_crosstable_results(
    db: Session, question1_id: int, question2_id: int
) -> List[CrosstableResult]:
    statement = text(
        """
        SELECT r1.response_value AS question1_value, r2.response_value AS question2_value, COUNT(*) AS count
        FROM responses r1
        JOIN responses r2 ON r1.participant_code = r2.participant_code
        WHERE r1.question_id = :question1_id AND r2.question_id = :question2_id
        GROUP BY r1.response_value, r2.response_value
    """
    )
    results = db.execute(
        statement, {"question1_id": question1_id, "question2_id": question2_id}
    ).fetchall()
    return [
        CrosstableResult(
            question1_value=row.question1_value,
            question2_value=row.question2_value,
            count=row.count,
        )
        for row in results
    ]
