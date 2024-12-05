-- database : school
--- 1) Ouvrir PgAdmin
--- 2) Databases -> Create -> Database
--- 3) database name : school
--- 4) Create table in public schemas

DROP TABLE IF EXISTS Teachers CASCADE;

-- Table 2: Teachers
CREATE TABLE Teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject VARCHAR(50)
);