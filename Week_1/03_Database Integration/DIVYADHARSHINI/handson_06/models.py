from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:DivyA%402005@localhost/college_db_orm"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

print("Connected successfully!")

#----------------------------------------------------------------------------

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Numeric,
    CheckConstraint
)
from sqlalchemy.orm import declarative_base, relationship


# Database Connection

DATABASE_URL = "mysql+mysqlconnector://root:DivyA%402005@localhost/college_db_orm"


engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

# Department Table
'''
class Department(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=False, unique=True)
    budget = Column(Numeric(12, 2))
'''
class Department(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=False, unique=True)
    budget = Column(Numeric(12, 2))

    students = relationship("Student", back_populates="department")
    professors = relationship("Professor", back_populates="department")

# Student Table

'''
class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    enrollment_year = Column(Integer)
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))
'''
class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    enrollment_year = Column(Integer)
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")

# Course Table

'''
class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_code = Column(String(20), unique=True)
    course_name = Column(String(100))
    credits = Column(Integer)
'''
class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_code = Column(String(20), unique=True)
    course_name = Column(String(100))
    credits = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="course")

# Professor Table

'''
class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    salary = Column(Numeric(10, 2))
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))
'''
class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    salary = Column(Numeric(10, 2))
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))

    department = relationship("Department", back_populates="professors")

# Enrollment Table

'''
class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    __table_args__ = (
        CheckConstraint(
            "grade IN ('A','B','C','D','F') OR grade IS NULL",
            name="chk_grade"
        ),
    )
'''

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    __table_args__ = (
        CheckConstraint(
            "grade IN ('A','B','C','D','F') OR grade IS NULL",
            name="chk_grade"
        ),
    )
    
print("Models created successfully!")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("All tables created successfully!")