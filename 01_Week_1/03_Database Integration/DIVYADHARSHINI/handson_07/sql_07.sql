CREATE DATABASE college_db_orm;

SHOW DATABASES;

USE college_db_orm;

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE enrollments;
TRUNCATE TABLE students;
TRUNCATE TABLE courses;
TRUNCATE TABLE professors;
TRUNCATE TABLE departments;

SET FOREIGN_KEY_CHECKS = 1;

SELECT * FROM departments;

USE college_db_orm;

-- STEP-85

SELECT first_name, enrollment_year
FROM students
WHERE email = 'divya@college.edu';

-- STEP-86

SELECT * FROM enrollments;

-- step - 97

USE college_db_orm;

SHOW TABLES;

SELECT * FROM alembic_version;

-- STEP-101

USE college_db_orm;

DESCRIBE students;

-- STPE-102

USE college_db_orm;

SHOW TABLES;
DESCRIBE course_schedules;

SHOW TABLES;