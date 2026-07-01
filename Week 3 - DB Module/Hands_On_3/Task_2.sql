CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    d.dept_name AS department,
    COUNT(e.course_id) AS courses_enrolled,
    ROUND(AVG(
        CASE 
            WHEN e.grade = 'A' THEN 4
            WHEN e.grade = 'B' THEN 3
            WHEN e.grade = 'C' THEN 2
            WHEN e.grade = 'D' THEN 1
            WHEN e.grade = 'F' THEN 0
            ELSE NULL
        END
    ), 2) AS gpa
FROM student s
LEFT JOIN departments d ON s.department_id = d.department_id
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name, d.dept_name;

select * from Vw_student_enrollment_summary;

CREATE VIEW vw_course_stats AS
SELECT 
    c.course_name,
    c.course_code,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(AVG(
        CASE 
            WHEN e.grade = 'A' THEN 4
            WHEN e.grade = 'B' THEN 3
            WHEN e.grade = 'C' THEN 2
            WHEN e.grade = 'D' THEN 1
            WHEN e.grade = 'F' THEN 0
            ELSE NULL
        END
    ), 2) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name, c.course_code;

select * from vw_course_stats;

SELECT * 
FROM vw_student_enrollment_summary 
WHERE gpa > 3.0;

UPDATE vw_student_enrollment_summary
SET department = 'Computer Science'
WHERE student_id = 1;

DROP VIEW IF EXISTS vw_course_stats;
DROP VIEW IF EXISTS vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    student_id,
    first_name,
    last_name,
    email,
    enrollment_year
FROM student
WHERE enrollment_year >= 2020
WITH CHECK OPTION;

select * from vw_student_enrollment_summary;