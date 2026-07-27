import { useState, useEffect } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";

import StudentProfile from "./components/StudentProfile";

import coursesData from "./data";

function App() {

  // Courses State
  const [courses, setCourses] = useState(coursesData);

  useEffect(() => {

    console.log("Courses updated");

    // This effect runs only when the courses state changes.
    // React compares the current value of 'courses' with the previous one.
    // If it has changed, the effect runs; otherwise, it is skipped.

  }, [courses]);

  // Search State
  const [searchTerm, setSearchTerm] = useState("");

  // Enrolled Courses State
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Loading State
  const [loading, setLoading] = useState(true);

  // Error State
  const [error, setError] = useState("");

  useEffect(() => {

    fetch("https://jsonplaceholder.typicode.com/posts?_limit=5")

    .then(response => {

        if (!response.ok) {

            throw new Error("Failed to fetch data");

        }

        return response.json();

    })

    .then(data => {

        console.log(data);

        setLoading(false);

    })

    .catch(error => {

        setError(error.message);

        setLoading(false);

    });

  }, []);

  // Enroll Handler
  const handleEnroll = (course) => {

    // Prevent duplicate enrollments
    const alreadyEnrolled = enrolledCourses.find(
      (item) => item.id === course.id
    );

    if (!alreadyEnrolled) {
      setEnrolledCourses([...enrolledCourses, course]);
    }

  };

  if (loading) {

    return (

        <h2 style={{textAlign:"center"}}>

            Loading...

        </h2>

    );

  }

  if (error) {

    return (

        <h2 style={{color:"red"}}>

            {error}

        </h2>

    );

  }

  return (
    <>

      <Header
    siteName="Student Portal"
    enrolledCount={enrolledCourses.length}
      />

      <main style={{ padding: "30px" }}>

        <h2>Available Courses</h2>

        <br />

        <input
          type="text"
          placeholder="Search courses..."
          value={searchTerm}
          onChange={(event) => setSearchTerm(event.target.value)}
          style={{
            padding: "10px",
            width: "300px",
            marginBottom: "25px",
            borderRadius: "5px"
          }}
        />

        <br />

        {courses
          .filter((course) =>
            course.name
              .toLowerCase()
              .includes(searchTerm.toLowerCase())
          )
          .map((course) => (
            <CourseCard
              key={course.id}
              {...course}
              onEnroll={handleEnroll}
            />
          ))}

        <hr />

        <h2>Enrolled Courses</h2>

        {enrolledCourses.length === 0 ? (
          <p>No courses enrolled yet.</p>
        ) : (
          <ul>
            {enrolledCourses.map((course) => (
              <li key={course.id}>
                {course.name} ({course.code})
              </li>
            ))}
          </ul>
        )}

        <StudentProfile />

      </main>

      <Footer />

    </>
  );
}

export default App;

//re-rendering - update the state, and React updates the UI for you.