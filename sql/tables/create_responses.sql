CREATE TABLE responses (
    idno INT PRIMARY KEY
    question_id INT REFERENCES questions()
    response_text TEXT
    response_value INT
);
