import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DivyA@2005",   
    database="college_db"
)

cursor = conn.cursor(dictionary=True)

start = time.time()

cursor.execute("""
SELECT
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON e.student_id = s.student_id
JOIN courses c
    ON e.course_id = c.course_id
""")

rows = cursor.fetchall()

for row in rows:
    print(
        row["enrollment_id"],
        row["first_name"],
        row["last_name"],
        row["course_name"]
    )

end = time.time()

print("\n----- Optimized JOIN Version -----")
print("Queries Executed: 1")
print("Execution Time:", end - start, "seconds")

cursor.close()
conn.close()