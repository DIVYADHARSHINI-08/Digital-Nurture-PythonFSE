from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from urllib.parse import quote_plus

from models import Student, Department, Enrollment


password = quote_plus("DivyA@2005")  

DATABASE_URL = (
    f"mysql+mysqlconnector://root:{password}@localhost/college_db_orm"
)

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

print("Session created successfully!")

# ---STEP 83---------

print("\nStudents in Computer Science Department:\n")

students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for student in students:
    print(
        student.student_id,
        student.first_name,
        student.last_name,
        student.email,
        student.enrollment_year
    )

#---STEP-84----

print("\nAll Enrollments:\n")

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:
    print(
        f"{enrollment.student.first_name} {enrollment.student.last_name}"
        f" --> "
        f"{enrollment.course.course_name}"
    )

#--STEP-85---

print("\nUpdating Student Enrollment Year...\n")

student = session.query(Student).filter_by(
    email="divya@college.edu"
).first()

if student:
    print(f"Before Update: {student.first_name} - {student.enrollment_year}")

    student.enrollment_year = 2025

    session.commit()

    print(f"After Update: {student.first_name} - {student.enrollment_year}")
else:
    print("Student not found.")

#---STEP-86----

print("\nDeleting one enrollment...\n")

enrollment = session.query(Enrollment).first()

if enrollment:
    print(
        f"Deleting Enrollment ID: {enrollment.enrollment_id}"
    )

    session.delete(enrollment)
    session.commit()

    print("Enrollment deleted successfully!")
else:
    print("No enrollment found.")

# ---STEP-87---

"""
N+1 Query Problem

1 query fetches all enrollments.
For each enrollment, SQLAlchemy issues additional queries
to fetch the related Student and Course objects.

Total:
1 + N + N queries
"""

# ----STEP-88---

print("\nUsing joinedload() to avoid N+1 Query Problem...\n")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for enrollment in enrollments:
    print(
        f"{enrollment.student.first_name} "
        f"{enrollment.student.last_name}"
        f" --> "
        f"{enrollment.course.course_name}"
    )

# ---STEP-89---

"""
Without joinedload():
1 query for enrollments
+ N queries for students
+ N queries for courses

Total ≈ 1 + N + N queries
"""

"""
With joinedload():
Only 1 SQL query retrieves
Enrollments + Students + Courses.
"""

# ---STEP-90---

"""
Comparison

Without joinedload():
---------------------
Many SQL queries were executed.
This is called the N+1 Query Problem.

With joinedload():
------------------
A single JOIN query retrieves all
Enrollment, Student and Course data.

Performance is much better because
database round-trips are reduced.
"""

# ---STEP-91---

"""
Bonus (Django ORM)

Equivalent code:

Enrollment.objects.select_related(
    'student',
    'course'
).all()
"""

