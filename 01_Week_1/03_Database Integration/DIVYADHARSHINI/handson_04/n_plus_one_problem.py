import mysql.connector
import time

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DivyA@2005",   
    database="college_db"
)

cursor = conn.cursor(dictionary=True)

query_count = 0

start = time.time()

# Query 1: Fetch all enrollments
cursor.execute("SELECT * FROM enrollments")
query_count += 1

enrollments = cursor.fetchall()

for enrollment in enrollments:
    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id = %s",
        (enrollment["student_id"],)
    )
    query_count += 1

    student = cursor.fetchone()

    print(
        enrollment["enrollment_id"],
        student["first_name"],
        student["last_name"]
    )

end = time.time()

print("\n----- N+1 Version -----")
print("Queries Executed:", query_count)
print("Execution Time:", end - start, "seconds")

cursor.close()
conn.close()