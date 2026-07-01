EXPLAIN 
SELECT s.first_name, s.last_name, c.course_name 
FROM enrollments e 
JOIN student s ON s.student_id = e.student_id 
JOIN courses c ON c.course_id = e.course_id 
WHERE s.enrollment_year = 2022;

-- The query shows the sequential scan on both the students and enrollments table

-- Cost: 12.16 to 42.16 & total rows examined are 1450

