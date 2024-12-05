-- database : school
--- 1) Ouvrir PgAdmin
--- 2) Databases -> Create -> Database
--- 3) database name : school
--- Create table in public schemas

DROP TABLE IF EXISTS Courses CASCADE;

-- Table 3: Courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    teacher_id INTEGER,
    course_name VARCHAR(50),
    FOREIGN KEY (teacher_id) REFERENCES Teachers (teacher_id)
);