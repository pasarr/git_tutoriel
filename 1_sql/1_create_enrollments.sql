-- database : school
--- 1) Ouvrir PgAdmin
--- 2) Databases -> Create -> Database
--- 3) database name : school
--- Create table in public schemas

DROP TABLE IF EXISTS Enrollments CASCADE;

-- Table 4: Enrollments
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students (student_id),
    FOREIGN KEY (course_id) REFERENCES Courses (course_id)
);
