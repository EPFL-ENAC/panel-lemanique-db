from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import SessionLocal
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
