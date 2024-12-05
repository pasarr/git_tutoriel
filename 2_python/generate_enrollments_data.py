import psycopg2
from random import randrange
from datetime import datetime

DB_NAME = "school"
DB_USER = "postgres"
DB_PASS = ""
DB_HOST = "localhost"
DB_PORT = 5432

# creation d'une connexion

conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)

cur = conn.cursor()

with conn:
    for course in range(20):
        # course_id
        cur.execute("""SELECT max(enrollment_id) FROM Enrollments""")       
        enrollment_id = cur.fetchall()
        enrollment_id_generate = enrollment_id[0][0] + 1

        # teacher_id
        cur.execute("""SELECT max(student_id) FROM students""")       
        student_id = cur.fetchall()
        student_id_generate = randrange(1,student_id[0][0])

        # course_id 
        cur.execute("""SELECT max(course_id) FROM courses""")       
        course_id = cur.fetchall()
        course_id_generate = randrange(1,course_id[0][0])

        #enrollment_date
        now = datetime.now()
        enrollment_date = now.strftime("%Y-%m-%d")

        cur.execute("INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (%s, %s, %s, %s)",
                (enrollment_id_generate,student_id_generate,course_id_generate,enrollment_date))

print("Insert Done!")