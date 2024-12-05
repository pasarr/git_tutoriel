TRUNCATE TABLE Courses CASCADE;

INSERT INTO Courses (course_id , teacher_id, course_name) VALUES
(1, 1, 'Mathematics'),
(2, 1, 'Mechanics'),
(3, 1, 'Algebra'),

(4, 2, 'English'),
(5, 2, 'Writing'),

(6, 3, 'Physics'),
(7, 3, 'Biology'),
(8, 3, 'Chemistry'),
(9, 3, 'Anatomy'),
(10, 3, 'Organic Chemistry'),

(11, 4, 'Hip-Hop'),
(12, 4, 'Jazz'),

(13, 5, '3D Printing'),
(14, 5, 'Painting'),

(15, 6, 'History'),
(16, 6, 'Geography'),
(17, 6, 'World War II'),
(18, 6, 'Political Geography'),

(19, 7, 'Computer Science'),
(20, 7, 'Database Systems'),
(21, 7, 'Data Science'),
(22, 7, 'Data Engineering');