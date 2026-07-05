from fastapi import FastAPI
from schemas import CourseCreate

from typing import Optional

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

courses = [
    {
        "id": 1,
        "name": "Python Programming",
        "code": "CS101",
        "credits": 4,
        "department_id": 1
    },
    {
        "id": 2,
        "name": "Data Structures",
        "code": "CS102",
        "credits": 4,
        "department_id": 1
    },
    {
        "id": 3,
        "name": "Web Development",
        "code": "IT201",
        "credits": 3,
        "department_id": 2
    }
]

@app.get("/")
async def root():
    return {"message": "API running"}


@app.post("/api/courses/")
async def create_course(course: CourseCreate):
    return {
        "message": "Course created successfully",
        "course": course
    }

from fastapi import HTTPException

@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(status_code=404, detail="Course not found")

@app.get("/api/courses/")
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None
):

    result = courses

    if department_id is not None:
        result = [
            c for c in result
            if c["department_id"] == department_id
        ]

    return result[skip: skip + limit]

@app.get("/testdb")
async def test_database(
    db: AsyncSession = Depends(get_db)
):
    return {"message": "Database connected"}