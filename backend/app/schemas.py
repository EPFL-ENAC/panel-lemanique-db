from pydantic import BaseModel
from datetime import date


class SurveyBase(BaseModel):
    survey_topic: str | None = None
    survey_date: date | None = None
    survey_name: str | None = None


class Survey(SurveyBase):
    survey_id: int

    class Config:
        from_attributes = True
