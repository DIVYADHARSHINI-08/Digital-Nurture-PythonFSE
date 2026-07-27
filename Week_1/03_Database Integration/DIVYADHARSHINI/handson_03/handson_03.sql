-- Task 1

SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);
-- -------------

SELECT
    c.course_name,
    c.course_code
FROM courses c
WHERE EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
)
AND NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND e.grade <> 'A'
);

-- ------------------

SELECT
    p.prof_name,
    p.salary,
    p.department_id
FROM professors p
WHERE salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

-- --------------

SELECT *
FROM
(
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM professors
    GROUP BY department_id
) AS dept_avg
WHERE avg_salary > 85000;

-- TASK - 2

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN e.grade = 'A' THEN 4
                WHEN e.grade = 'B' THEN 3
                WHEN e.grade = 'C' THEN 2
                WHEN e.grade = 'D' THEN 1
                WHEN e.grade = 'F' THEN 0
            END
        ),2
    ) AS gpa
FROM students s
JOIN departments d
ON s.department_id = d.department_id
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY
    s.student_id,
    s.first_name,
    s.last_name,
    d.dept_name; 
    
SELECT * FROM vw_student_enrollment_summary;

CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY
    c.course_id,
    c.course_name,
    c.course_code;
    

SELECT * FROM vw_course_stats;

SELECT *
FROM vw_student_enrollment_summary
WHERE gpa > 3.0;

UPDATE vw_student_enrollment_summary
SET student_name='Rahul'
WHERE student_id=1;

-- Multi-table views containing JOIN, GROUP BY, and aggregate
-- functions are generally not updatable because MySQL cannot
-- map changes back to the underlying base tables.

DROP VIEW IF EXISTS vw_student_enrollment_summary;

DROP VIEW IF EXISTS vw_course_stats;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    department_id
FROM students
WHERE department_id = 1
WITH CHECK OPTION;

SELECT *
FROM vw_student_enrollment_summary;

UPDATE vw_student_enrollment_summary
SET department_id = 2
WHERE student_id = 1;

-- Task - 3B

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN

    DECLARE enroll_count INT;

    SELECT COUNT(*)
    INTO enroll_count
    FROM enrollments
    WHERE student_id = p_student_id
      AND course_id = p_course_id;

    IF enroll_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Student is already enrolled in this course';
    ELSE
        INSERT INTO enrollments
        (student_id, course_id, enrollment_date)
        VALUES
        (p_student_id, p_course_id, p_enrollment_date);
    END IF;

END$$

DELIMITER ;

CALL sp_enroll_student(9,2,'2024-01-15');

CALL sp_enroll_student(1,1,'2024-01-15');

CREATE TABLE department_transfer_log
(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_department INT
)
BEGIN

    DECLARE old_dept INT;

    START TRANSACTION;

    SELECT department_id
    INTO old_dept
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log
    (student_id, old_department, new_department)
    VALUES
    (p_student_id, old_dept, p_new_department);

    COMMIT;

END$$

DELIMITER ;

-- -------------------

CALL sp_transfer_student(1,2);

SELECT *
FROM department_transfer_log;

CALL sp_transfer_student(1,100);

-- savepoint

START TRANSACTION;

INSERT INTO enrollments
(student_id,course_id,enrollment_date)
VALUES
(9,3,CURDATE());

SAVEPOINT first_insert;

INSERT INTO enrollments
(student_id,course_id,enrollment_date)
VALUES
(999,1,CURDATE());

ROLLBACK TO SAVEPOINT first_insert;

COMMIT;

SELECT *
FROM enrollments
WHERE student_id = 9;


