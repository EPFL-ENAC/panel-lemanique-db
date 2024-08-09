import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# noqa F401 is necessary to avoid having ruff automatically remove the unused imports
from models.base import Base  # noqa F401
from models.participant_labels import ParticipantLabels  # noqa F401
from models.participants import Participants  # noqa F401
from models.question_labels import QuestionLabels  # noqa F401
from models.questions import Questions  # noqa F401
from models.responses import Responses  # noqa F401
from models.sections import Sections  # noqa F401
from models.surveys import Surveys  # noqa F401
from models.survey_completion import SurveyCompletion  # noqa F401
from models.survey_completion_labels import SurveyCompletionLabels  # noqa F401

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
