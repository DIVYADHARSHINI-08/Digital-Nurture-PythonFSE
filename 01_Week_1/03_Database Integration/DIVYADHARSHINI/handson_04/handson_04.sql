-- TASK - 1

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- STEP 49
-- The EXPLAIN output was checked.
-- Tables showing type = 'ALL' perform a Full Table Scan.
-- This indicates MySQL scans every row because no suitable index exists.

-- STEP 50
-- Rows examined are shown in the 'rows' column of EXPLAIN.
-- A larger number of examined rows usually indicates lower query efficiency.
-- Creating indexes can reduce the number of rows MySQL scans.

-- TASK - 2

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

SHOW INDEX FROM students;

CREATE UNIQUE INDEX idx_enrollment_unique
ON enrollments(student_id, course_id);

SHOW INDEX
FROM enrollments;

INSERT INTO enrollments
(student_id, course_id, enrollment_date)
VALUES
(1,1,CURDATE());

-- STEP 52
-- Created a composite UNIQUE index on (student_id, course_id).
-- This improves lookup performance and prevents duplicate enrollments.

-- TASK - 2

CREATE INDEX idx_course_code
ON courses(course_code);

SHOW INDEX FROM courses;

-- STEP 53
-- Created an index on courses(course_code).
-- This improves performance for queries filtering by course_code.

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- STEP 54
-- Re-ran EXPLAIN after creating indexes.
-- MySQL now uses idx_students_enrollment_year for filtering.
-- The query scans fewer rows than before.
-- Query performance is improved because an index is used instead of a full table scan.

