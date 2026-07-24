import { useDispatch, useSelector } from "react-redux";
import { unenroll } from "../features/enrollmentSlice";

function ProfilePage() {

    const dispatch = useDispatch();

    const enrolledCourses = useSelector(

        (state) => state.enrollment.enrolledCourses

    );
    return (

        <div>

            <h1>Student Profile</h1>

            <h2>Enrolled Courses</h2>

            {

                enrolledCourses.length === 0 ?

                (

                    <p>No courses enrolled.</p>

                )

                :

                (

                    <ul>

                        {

                            enrolledCourses.map((course) => (

                                <li key={course.id}>

                                    {course.name}

                                    <button
                                        onClick={() => dispatch(unenroll(course.id))}
                                        style={{
                                            marginLeft: "15px"
                                        }}
                                    >
                                        Remove
                                    </button>

                                </li>

                            ))

                        }

                    </ul>

                )

            }

        </div>

    );

}

export default ProfilePage;







/* import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function ProfilePage() {

    const {
        enrolledCourses,
        removeCourse
    } = useContext(EnrollmentContext);

    return (

        <div>

            <h1>Student Profile</h1>

            <h2>Enrolled Courses</h2>

            {
                enrolledCourses.length === 0 ? (

                    <p>No courses enrolled.</p>

                ) : (

                    <ul>

                        {
                            enrolledCourses.map((course) => (

                                <li key={course.id}>

                                    <strong>{course.name}</strong>

                                    <button
                                        onClick={() => removeCourse(course.id)}
                                        style={{
                                            marginLeft: "15px",
                                            padding: "5px 10px",
                                            cursor: "pointer"
                                        }}
                                    >
                                        Remove
                                    </button>

                                </li>

                            ))
                        }

                    </ul>

                )
            }

        </div>

    );

}

export default ProfilePage;

*/


/*import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function ProfilePage() {

    const { enrolledCourses } = useContext(EnrollmentContext);

    return (

        <div>

            <h1>Student Profile</h1>

            <h2>Enrolled Courses</h2>

            {

                enrolledCourses.length === 0 ?

                    <p>No courses enrolled.</p>

                :

                    <ul>

                        {

                            enrolledCourses.map((course) => (

                                <li key={course.id}>

                                    {course.name}

                                </li>

                            ))

                        }

                    </ul>

            }

        </div>

    );

}

export default ProfilePage;
*/