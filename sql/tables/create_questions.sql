CREATE TABLE questions (
    question_id INT PRIMARY KEY
    section_id INT REFERENCES sections(section_id)
    response_text TEXT
    response_value INT
);
