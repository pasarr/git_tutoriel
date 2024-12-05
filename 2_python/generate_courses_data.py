import psycopg2
from random import randrange

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

courses = ["Sustainable and Renewable Energy" ,"Industrial and Organizational Psychology" ,"Atmospheric Sciences" ,"Game Design"
,"Epidemiology","The Internet of Things","Robotics","Artificial Intelligence","Health Information Technology","Mechatronics"
,"Chemical Engineering","Nursing","Biomedical Engineering","Computational Linguistics","Information Technology"
,"Big Data","Construction Management","Electrical Engineering","Drone Technology","Data Analytics and Business Intelligence"]

with conn:
    for course in courses:    
        # course_id
        cur.execute("""SELECT max(course_id) FROM Courses""")       
        course_id = cur.fetchall()
        course_id_generate = course_id[0][0] + 1

        # teacher_id
        cur.execute("""SELECT max(teacher_id) FROM Courses""")       
        teacher_id = cur.fetchall()
        teacher_id_generate = randrange(1,teacher_id[0][0])

        cur.execute("INSERT INTO Courses (course_id , teacher_id, course_name) VALUES (%s, %s, %s)",
                (course_id_generate, teacher_id_generate, course))

print("Insert Done!")