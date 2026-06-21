select CONCAT(s.first_name, ' ', s.last_name), d.dept_name from student as s join departments as d on s.department_id= d.department_id; 

SELECT 
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name,
    c.course_code,
    e.grade
FROM enrollments e
JOIN student s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

SELECT 
    s.student_id,
    s.first_name,
    s.last_name,
    s.email
FROM student s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.student_id IS NULL;


SELECT 
    c.course_id,
    c.course_code,
    c.course_name,
    COUNT(e.enrollment_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_code, c.course_name
ORDER BY total_students DESC;


SELECT 
    departments.dept_name,
    professors.prof_name,
    professors.salary
FROM departments
LEFT JOIN professors ON departments.department_id = professors.department_id;