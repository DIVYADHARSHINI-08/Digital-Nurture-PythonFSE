import { Link, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";

import courses from "../data/data";
import { enroll } from "../features/enrollmentSlice";

function CoursesPage() {

    const navigate = useNavigate();

    const dispatch = useDispatch();

    const handleEnroll = (course) => {

        dispatch(enroll(course));

        navigate("/profile");

    };

    return (

        <div>

            <h1>Courses</h1>

            {

                courses.map((course) => (

                    <div
                        key={course.id}
                        style={{
                            border: "1px solid gray",
                            padding: "15px",
                            marginBottom: "15px"
                        }}
                    >

                        <h3>{course.name}</h3>

                        <p>Credits : {course.credits}</p>

                        <Link to={`/courses/${course.id}`}>

                            View Details

                        </Link>

                        <br /><br />

                        <button
                            onClick={() => handleEnroll(course)}
                        >
                            Enroll
                        </button>

                    </div>

                ))

            }

        </div>

    );

}

export default CoursesPage;



/*import { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import courses from "../data/data";
import { EnrollmentContext } from "../context/EnrollmentContext";

function CoursesPage() {

    const navigate = useNavigate();

    const { enrollCourse } = useContext(EnrollmentContext);

    const handleEnroll = (course) => {

        enrollCourse(course);

        navigate("/profile");

    };

    return (

        <div>

            <h1>Courses</h1>

            {

                courses.map((course) => (

                    <div
                        key={course.id}
                        style={{
                            border: "1px solid gray",
                            padding: "15px",
                            marginBottom: "15px"
                        }}
                    >

                        <h3>{course.name}</h3>

                        <p>Credits: {course.credits}</p>

                        <Link to={`/courses/${course.id}`}>
                            View Details
                        </Link>

                        <br /><br />

                        <button onClick={() => handleEnroll(course)}>
                            Enroll
                        </button>

                    </div>

                ))

            }

        </div>

    );
}

export default CoursesPage; */

/*import { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";

import courses from "../data/data";
import { EnrollmentContext } from "../context/EnrollmentContext";

function CoursesPage() {

    const navigate = useNavigate();

    const {
        enrolledCourses,
        setEnrolledCourses
    } = useContext(EnrollmentContext);

    const handleEnroll = (course) => {

        setEnrolledCourses([...enrolledCourses, course]);

        navigate("/profile");

    };

    return (

        <div>

            <h1>Courses</h1>

            {

                courses.map((course) => (

                    <div
                        key={course.id}
                        style={{
                            border: "1px solid gray",
                            padding: "15px",
                            marginBottom: "15px"
                        }}
                    >

                        <h3>{course.name}</h3>

                        <p>Credits : {course.credits}</p>

                        <Link to={`/courses/${course.id}`}>
                            View Details
                        </Link>

                        <br /><br />

                        <button onClick={() => handleEnroll(course)}>
                            Enroll
                        </button>

                    </div>

                ))

            }

        </div>

    );

}

export default CoursesPage;
*/