from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://127.0.0.1:5001"
STUDENT_SERVICE = "http://127.0.0.1:5002"


@app.route("/api/courses", methods=["GET"])
def get_courses():

    response = requests.get(
        f"{COURSE_SERVICE}/api/courses"
    )

    return jsonify(response.json())


@app.route("/api/students", methods=["GET"])
def get_students():

    response = requests.get(
        f"{STUDENT_SERVICE}/api/students"
    )

    return jsonify(response.json())


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):

    response = requests.post(
        f"{STUDENT_SERVICE}/api/students/{id}/enroll",
        json=request.get_json()
    )

    return (
        jsonify(response.json()),
        response.status_code
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)