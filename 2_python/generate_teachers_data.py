import psycopg2
from faker import Faker

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

subjects = ["Mathematics"
, "English"
, "Science"
, "Music"
, "Art"
, "History"
, "IT"]

# init un generateur
fake = Faker()

with conn:
    for subject in subjects:
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # teacher_id
        cur.execute("""SELECT max(teacher_id) FROM teachers""")       
        teacher_id = cur.fetchall()
        teacher_id_generate = teacher_id[0][0] + 1
        
        cur.execute("INSERT INTO teachers VALUES (%s, %s, %s ,%s)", (teacher_id_generate, first_name
        , last_name, subject))

print("Insert Done!")