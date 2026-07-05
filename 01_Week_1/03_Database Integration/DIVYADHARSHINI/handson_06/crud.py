from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

from models import (
    Base,
    Department,
    Student,
    Course,
    Enrollment,
    Professor
)


password = quote_plus("DivyA@2005")  

DATABASE_URL = (
    f"mysql+mysqlconnector://root:{password}@localhost/college_db_orm"
)

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

print("Session created successfully!")


# Insert Departments

cs = Department(
    dept_name="Computer Science",
    budget=850000
)

ec = Department(
    dept_name="Electronics",
    budget=620000
)

me = Department(
    dept_name="Mechanical",
    budget=540000
)

session.add_all([cs, ec, me])
session.commit()

print("Departments inserted successfully!")


# Insert Students

s1 = Student(
    first_name="Divya",
    last_name="Dharshini",
    email="divya@college.edu",
    enrollment_year=2022,
    department=cs
)

s2 = Student(
    first_name="Rahul",
    last_name="Sharma",
    email="rahul@college.edu",
    enrollment_year=2022,
    department=cs
)

s3 = Student(
    first_name="Priya",
    last_name="Nair",
    email="priya@college.edu",
    enrollment_year=2023,
    department=ec
)

s4 = Student(
    first_name="Arun",
    last_name="Kumar",
    email="arun@college.edu",
    enrollment_year=2023,
    department=me
)

s5 = Student(
    first_name="Sneha",
    last_name="Reddy",
    email="sneha@college.edu",
    enrollment_year=2024,
    department=cs
)

session.add_all([s1, s2, s3, s4, s5])
session.commit()


# Insert Courses


c1 = Course(
    course_code="CS101",
    course_name="Database Systems",
    credits=4
)

c2 = Course(
    course_code="CS102",
    course_name="Data Structures",
    credits=3
)

c3 = Course(
    course_code="CS103",
    course_name="Operating Systems",
    credits=4
)

session.add_all([c1, c2, c3])
session.commit()

print("Courses inserted successfully!")


# Insert Enrollments

e1 = Enrollment(
    student=s1,
    course=c1,
    grade="A"
)

e2 = Enrollment(
    student=s2,
    course=c1,
    grade="B"
)

e3 = Enrollment(
    student=s3,
    course=c2,
    grade="A"
)

e4 = Enrollment(
    student=s5,
    course=c3,
    grade="B"
)

session.add_all([e1, e2, e3, e4])
session.commit()

print("Enrollments inserted successfully!")

print("Students inserted successfully!")

