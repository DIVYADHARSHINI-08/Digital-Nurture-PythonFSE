import { useParams } from "react-router-dom";

import courses from "../data/data";

function CourseDetailPage() {

    const { courseId } = useParams();

    const course = courses.find(

        (course) => course.id === Number(courseId)

    );

    if (!course) {

        return <h2>Course Not Found</h2>;

    }

    return (

        <div>

            <h1>Course Details</h1>

            <h2>{course.name}</h2>

            <p><strong>Credits:</strong> {course.credits}</p>

            <p><strong>Instructor:</strong> {course.instructor}</p>

            <p><strong>Description:</strong> {course.description}</p>

        </div>

    );

}

export default CourseDetailPage;