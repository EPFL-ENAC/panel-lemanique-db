from fastapi import Depends, FastAPI, HTTPException
from typing import List
from sqlalchemy.orm import Session
from backend.database.database import SessionLocal
from .schemas import CrosstableResult
from . import crud

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/surveys/")
def read_surveys(limit: int = 100, db: Session = Depends(get_db)):
    surveys = crud.get_surveys(db, limit=limit)
    return surveys


@app.get("/surveys/{survey_id}")
def read_survey(survey_id: int, db: Session = Depends(get_db)):
    db_survey = crud.get_survey(db, survey_id=survey_id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return db_survey


@app.get("/sections/")
def read_sections(limit: int = 100, db: Session = Depends(get_db)):
    sections = crud.get_sections(db, limit=limit)
    return sections


@app.get("/questions/")
def read_questions(limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, limit=limit)
    return questions


@app.get("/responses/")
def read_responses(limit: int = 100, db: Session = Depends(get_db)):
    responses = crud.get_responses(db, limit=limit)
    return responses


@app.get("/responses/{participant_code}")
def read_responses_for_participant(
    participant_code: str, limit: int = 10, db: Session = Depends(get_db)
):
    responses = crud.get_responses_for_participant(
        db, participant_code=participant_code, limit=limit
    )
    return responses


@app.get("/participants/{participant_code}")
def read_participant(participant_code: str, db: Session = Depends(get_db)):
    db_participant = crud.get_participant(db, participant_code=participant_code)
    if db_participant is None:
        raise HTTPException(status_code=404, detail="Participant not found")
    return db_participant


@app.get("/crosstable/", response_model=List[CrosstableResult])
def read_crosstable(
    question1_id: int, question2_id: int, db: Session = Depends(get_db)
):
    return crud.get_crosstable_results(db, question1_id, question2_id)
