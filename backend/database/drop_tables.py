from database import engine

# noqa F401 is necessary to avoid having ruff automatically remove the unused imports
from models.base import Base
from models.participant_labels import ParticipantLabels  # noqa F401
from models.participants import Participants  # noqa F401
from models.question_labels import QuestionLabels  # noqa F401
from models.questions import Questions  # noqa F401
from models.responses import Responses  # noqa F401
from models.sections import Sections  # noqa F401
from models.surveys import Surveys  # noqa F401
from models.survey_completion import SurveyCompletion  # noqa F401
from models.survey_completion_labels import SurveyCompletionLabels  # noqa F401

Base.metadata.drop_all(engine)
