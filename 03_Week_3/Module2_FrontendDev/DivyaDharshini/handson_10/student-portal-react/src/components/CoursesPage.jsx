import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  fetchAllCourses,
  selectCourses,
  selectCoursesLoading,
  selectCoursesError,
} from "../features/courses/courseSlice";

function CoursesPage() {

  const dispatch = useDispatch();

  const courses = useSelector(selectCourses);

    const loading = useSelector(selectCoursesLoading);

    const error = useSelector(selectCoursesError);

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>{error}</h2>;
  }

  return (
    <div>
      <h1>Courses</h1>

      {courses.map(course => (
        <div key={course.id}>
          <h3>{course.title}</h3>
        </div>
      ))}
    </div>
  );
}

export default CoursesPage;