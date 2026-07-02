from fastapi import FastAPI
from schemas import *

from fastapi import FastAPI, HTTPException, status, BackgroundTasks
from schemas import *

'''
app = FastAPI(
    title="Course Management API",
    version="1.0"
)
'''

app = FastAPI(
    title="Course Management API",
    description="REST API for managing courses, students, and enrollments.",
    version="1.0",
    contact={
        "name": "Divya Dharshini",
        "email": "divya@example.com"
    }
)

courses = []
students = []
enrollments = []

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")

@app.get("/")
async def root():
    return {"message": "API Running"}

@app.post(
    "/api/courses/",
    tags=["Courses"],
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new course",
    response_description="Course created successfully"
)
async def create_course(course: CourseCreate):

    new_course = {
        "id": len(courses) + 1,
        "name": course.name,
        "code": course.code,
        "credits": course.credits,
        "department_id": course.department_id
    }

    courses.append(new_course)

    return new_course

@app.get(
    "/api/courses/",
    response_model=list[CourseResponse]
    ,
    tags=["Courses"]
)
async def get_courses():
    return courses

@app.get(
    "/api/courses/{id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def get_course(id: int):

    for course in courses:
        if course["id"] == id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )

@app.put(
    "/api/courses/{id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def update_course(
    id: int,
    course: CourseUpdate
):

    for c in courses:

        if c["id"] == id:

            if course.name is not None:
                c["name"] = course.name

            if course.code is not None:
                c["code"] = course.code

            if course.credits is not None:
                c["credits"] = course.credits

            if course.department_id is not None:
                c["department_id"] = course.department_id

            return c

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )

@app.delete(
    "/api/courses/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(id: int):

    for course in courses:

        if course["id"] == id:

            courses.remove(course)

            return

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )

@app.get("/api/courses/{id}/students/", response_model=list[StudentResponse], tags=["Courses"])
async def get_course_students(id: int):

    # Check if course exists
    course_exists = any(course["id"] == id for course in courses)

    if not course_exists:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    enrolled_students = []

    for enrollment in enrollments:

        if enrollment["course_id"] == id:

            for student in students:

                if student["id"] == enrollment["student_id"]:
                    enrolled_students.append(student)

    return enrolled_students

##students

@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"]
)
async def create_student(student: StudentCreate):

    new_student = {
        "id": len(students) + 1,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "email": student.email
    }

    students.append(new_student)

    return new_student

@app.get(
    "/api/students/",
    response_model=list[StudentResponse],
    tags=["Students"]
)
async def get_students():
    return students

@app.get(
    "/api/students/{id}",
    response_model=StudentResponse,
    tags=["Students"]
)
async def get_student(id: int):

    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.put(
    "/api/students/{id}",
    response_model=StudentResponse,
    tags=["Students"]
)
async def update_student(id: int, student: StudentCreate):

    for s in students:

        if s["id"] == id:

            s["first_name"] = student.first_name
            s["last_name"] = student.last_name
            s["email"] = student.email

            return s

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.delete(
    "/api/students/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Students"]
)
async def delete_student(id: int):

    for student in students:

        if student["id"] == id:

            students.remove(student)
            return

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

##Enrollement 

@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]    
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks
):

    new_enrollment = {
        "id": len(enrollments) + 1,
        "student_id": enrollment.student_id,
        "course_id": enrollment.course_id
    }

    enrollments.append(new_enrollment)

    student_email = None

    for student in students:
        if student["id"] == enrollment.student_id:
            student_email = student["email"]
            break

    if student_email:
        background_tasks.add_task(
            send_confirmation_email,
            student_email
        )

    return new_enrollment

@app.get(
    "/api/enrollments/",
    response_model=list[EnrollmentResponse],
    tags=["Enrollments"]
)
async def get_enrollments():
    return enrollments


@app.get(
    "/api/enrollments/{id}",
    response_model=EnrollmentResponse,
    tags=["Enrollments"]    
)
async def get_enrollment(id: int):

    for enrollment in enrollments:
        if enrollment["id"] == id:
            return enrollment

    raise HTTPException(
        status_code=404,
        detail="Enrollment not found"
    )


@app.put(
    "/api/enrollments/{id}",
    response_model=EnrollmentResponse,
    tags=["Enrollments"]
)
async def update_enrollment(id: int, enrollment: EnrollmentCreate):

    for e in enrollments:

        if e["id"] == id:

            e["student_id"] = enrollment.student_id
            e["course_id"] = enrollment.course_id

            return e

    raise HTTPException(
        status_code=404,
        detail="Enrollment not found"
    )

@app.delete(
    "/api/enrollments/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Enrollments"]    
)
async def delete_enrollment(id: int):

    for enrollment in enrollments:

        if enrollment["id"] == id:

            enrollments.remove(enrollment)
            return

    raise HTTPException(
        status_code=404,
        detail="Enrollment not found"
    )