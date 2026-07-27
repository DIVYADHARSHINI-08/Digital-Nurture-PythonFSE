import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {

    const [enrolledCourses, setEnrolledCourses] = useState([]);

    // Enroll a course
    const enrollCourse = (course) => {

        setEnrolledCourses((prevCourses) => {

            // Prevent duplicate enrollment
            if (prevCourses.some((c) => c.id === course.id)) {
                return prevCourses;
            }

            return [...prevCourses, course];

        });

    };

    // Remove a course
    const removeCourse = (courseId) => {

        setEnrolledCourses((prevCourses) =>
            prevCourses.filter((course) => course.id !== courseId)
        );

    };

    return (

        <EnrollmentContext.Provider
            value={{
                enrolledCourses,
                enrollCourse,
                removeCourse
            }}
        >
            {children}
        </EnrollmentContext.Provider>

    );

}