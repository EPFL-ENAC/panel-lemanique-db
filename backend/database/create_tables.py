from database import engine

# noqa F401 is necessary to avoid having ruff automatically remove the unused imports
from models.base import Base  # noqa F401
from models.participant_label import ParticipantLabel  # noqa F401
from models.participant import Participant  # noqa F401
from models.question_label import QuestionLabel  # noqa F401
from models.question import Question  # noqa F401
from models.response import Response  # noqa F401
from models.section import Section  # noqa F401
from models.survey import Survey  # noqa F401
from models.survey_completion import SurveyCompletion  # noqa F401
from models.survey_completion_label import SurveyCompletionLabel  # noqa F401

Base.metadata.create_all(engine)
