CREATE DATABASE college_db;

USE college_db;

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,

    CONSTRAINT fk_student_department
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,

    CONSTRAINT fk_course_department
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),

    CONSTRAINT fk_enrollment_student
    FOREIGN KEY (student_id)
    REFERENCES students(student_id),

    CONSTRAINT fk_enrollment_course
    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
);

CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),

    CONSTRAINT fk_prof_department
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

SHOW TABLES;

DESCRIBE departments;

DESCRIBE students;

DESCRIBE courses;

DESCRIBE enrollments;

DESCRIBE professors;

-- ---------------------- DOCUMENTATION ------------------------------

-- 1NF Verification
-- All tables contain atomic values.
-- Every column stores a single value.
-- No repeating groups or multiple phone numbers are stored in one field.

-- 2NF Verification
-- Every non-key attribute depends on the complete key.
-- In enrollments, grade and enrollment_date depend on the student-course combination.
-- No partial dependency exists.

-- 3NF Verification
-- No transitive dependency exists.
-- Department information is stored only in the departments table.
-- Students reference departments using department_id.
-- This avoids data redundancy and update anomalies.

-- 3NF Analysis for Enrollments
-- The enrollments table stores only enrollment-related information.
-- Grade and enrollment_date depend directly on the enrollment record.
-- Student and course details are stored in separate tables.
-- Therefore, the table satisfies Third Normal Form.

ALTER TABLE students
ADD phone_number VARCHAR(15);

DESCRIBE students;

ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

DESCRIBE courses;

ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

DESCRIBE departments;

ALTER TABLE students
DROP COLUMN phone_number;

DESCRIBE students;



