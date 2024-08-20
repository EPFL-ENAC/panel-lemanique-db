import pandas as pd
from ..database.database import engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from ..database.models.survey import Survey
from ..database.models.section import Section
from ..database.models.question import Question
from ..database.models.survey_completion import SurveyCompletion  # noqa F401
from ..database.models.participant import Participant  # noqa F401
from ..database.models.response import Response  # noqa F401

Session = sessionmaker(bind=engine)
session = Session()

try:
    survey = Survey(survey_name="Vague 2", survey_topic="Consommation")
    session.add(survey)
    session.commit()

    survey_id = survey.id

    data_path = "data_preprocessing/data/wave2/"

    sections = pd.read_csv(data_path + "sections.tsv", sep="\t")
    sections = sections.assign(survey_id=survey_id)

    sections.to_sql(
        "sections",
        con=engine,
        method="multi",
        schema="public",
        if_exists="append",
        index=False,
    )

    # Prepare ingestion of questions
    section_ids = pd.read_sql(
        select(Section.id, Section.section_name).where(Section.survey_id == survey_id),
        con=engine,
    )

    questions = pd.read_csv(data_path + "questions.tsv", sep="\t")
    questions = questions.merge(
        section_ids, on="section_name", how="left"
    )  # If NAs are present, section_id will be cast to float
    questions = questions.drop("section_name", axis=1).rename(
        columns={"id": "section_id"}
    )

    questions.to_sql(
        "questions",
        con=engine,
        method="multi",
        schema="public",
        if_exists="append",
        index=False,
    )

    # Prepare ingestion of question labels
    query = (
        select(Question.id, Question.question_code)
        .join(Section, Question.section_id == Section.id)
        .where(Section.survey_id == survey_id)
    )

    question_codes = pd.read_sql(query, con=engine)
    question_labels = pd.read_csv(data_path + "question_labels.tsv", sep="\t")
    question_labels = (
        question_labels.merge(question_codes, on="question_code", how="left")
        .drop("question_code", axis=1)
        .rename(columns={"id": "question_id"})
    )

    question_labels.to_sql(
        "question_labels",
        con=engine,
        method="multi",
        schema="public",
        if_exists="append",
        index=False,
    )

    # Prepare ingestion of participants
    participants = (
        pd.read_csv(data_path + "participants.tsv", sep="\t")
        .drop(
            ["pays", "weight", "titre_source", "cp_source", "localite_source"], axis=1
        )
        .convert_dtypes()
    )  # NaNs will be read as float, but convert_dtypes uses pd.NA and Int64

    participants.to_sql(
        "participants",
        con=engine,
        method="multi",
        schema="public",
        if_exists="append",
        index=False,
    )

    # Prepare ingestion of survey completion
    survey_completion = (
        pd.read_csv(
            data_path + "survey_completion.tsv",
            sep="\t",
            parse_dates=["start_date", "end_date"],
        )
        .convert_dtypes()
        .drop("flag_troll", axis=1)
        .assign(survey_id=survey_id)
    )

    survey_completion.to_sql(
        "survey_completion",
        con=engine,
        method="multi",
        schema="public",
        if_exists="append",
        index=False,
    )

    # Prepare ingestion of responses
    responses = pd.read_csv(
        data_path + "responses.tsv", sep="\t", dtype={"response_text": "str"}
    ).convert_dtypes()

    responses = (
        responses.merge(question_codes, on="question_code", how="left")
        .drop("question_code", axis=1)
        .rename(columns={"id": "question_id"})
    )

    responses.iloc[:10000].to_sql(
        "responses",
        con=engine,
        method="multi",
        schema="public",
        if_exists="append",
        index=False,
    )

except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()
