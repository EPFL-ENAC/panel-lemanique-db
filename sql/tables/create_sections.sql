CREATE TABLE sections (
    section_id INT PRIMARY KEY
    section_topic TEXT
    section_name TEXT
    survey_id INT REFERENCES surveys(survey_id)
);
