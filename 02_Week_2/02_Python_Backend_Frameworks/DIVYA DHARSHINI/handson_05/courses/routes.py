'''
from flask import Blueprint

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

'''
from flask import Blueprint, jsonify, request
from extensions import db
from courses.models import Course, Department, Student, Enrollment


courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["name", "code", "credits", "department_id"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    department = Department.query.get(data["department_id"])

    if department is None:
        return jsonify({"error": "Department not found"}), 404

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department=department
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201

@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get_or_404(id)

    return jsonify(course.to_dict())

@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data.get("name", course.name)
    course.code = data.get("code", course.code)
    course.credits = data.get("credits", course.credits)

    db.session.commit()

    return jsonify(course.to_dict())

@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    }), 200

@courses_bp.route("/<int:id>/students/", methods=["GET"])
def get_course_students(id):

    course = Course.query.get_or_404(id)

    students = (
        Student.query
        .join(Enrollment)
        .filter(Enrollment.course_id == course.id)
        .all()
    )

    return jsonify([student.to_dict() for student in students])