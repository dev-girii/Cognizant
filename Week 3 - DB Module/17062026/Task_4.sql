select count(e.course_id) as total_enrolled, c.course_name from enrollments as e join courses as c on c.course_id = e.course_id group by c.course_id;

SELECT 
    Round(AVG(p.Salary),2) AS "AVG_Salary", 
    d.dept_name 
FROM professors AS p 
JOIN departments AS d ON p.department_id = d.department_id 
GROUP BY p.department_id, d.dept_name;

SELECT 
    department_id, 
    dept_name, 
    budget 
FROM departments 
WHERE budget > 600000;

SELECT 
    e.grade, 
    COUNT(*) AS student_count
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade
ORDER BY e.grade ASC;

SELECT 
    d.department_id,
    d.dept_name,
    COUNT(e.enrollment_id) AS total_enrolled_students
FROM departments d
JOIN courses c ON d.department_id = c.department_id
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(e.enrollment_id) > 2;

