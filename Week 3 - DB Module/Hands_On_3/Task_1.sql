SELECT 
    s.student_id,
    s.first_name,
    s.last_name,
    COUNT(e.course_id) AS enrollment_count
FROM student s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) > (
    SELECT AVG(student_total_courses)
    FROM (
        SELECT COUNT(course_id) AS student_total_courses
        FROM enrollments
        GROUP BY student_id
    ) AS overall_avg
);

SELECT 
    c.course_id,
    c.course_code,
    c.course_name
FROM courses c
WHERE EXISTS (
    SELECT 1 FROM enrollments e_check WHERE e_check.course_id = c.course_id
) AND NOT EXISTS (
    SELECT 1 
    FROM enrollments e 
    WHERE e.course_id = c.course_id 
      AND (e.grade <> 'A' OR e.grade IS NULL)
);


SELECT 
    p1.professor_id,
    p1.prof_name,
    p1.department_id,
    p1.salary
FROM professors p1
WHERE p1.salary = (
    SELECT MAX(p2.salary) 
    FROM professors p2 
    WHERE p2.department_id = p1.department_id
);

SELECT 
    dept_salaries.dept_name,
    dept_salaries.avg_salary
FROM (
    SELECT 
        d.dept_name,
        AVG(p.salary) AS avg_salary
    FROM departments d
    JOIN professors p ON d.department_id = p.department_id
    GROUP BY d.department_id, d.dept_name
) AS dept_salaries
WHERE dept_salaries.avg_salary > 85000;