CREATE TABLE question_labels (
    label_id INT PRIMARY KEY
    question_id INT REFERENCES questions(question_id)
    label_text TEXT
    label_value INT
);
