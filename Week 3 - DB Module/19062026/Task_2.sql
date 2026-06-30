CREATE INDEX idx_student_enrollment_year 
ON student(enrollment_year);

CREATE UNIQUE INDEX uq_enrollments_student_course 
ON enrollments(student_id, course_id);

CREATE INDEX idx_courses_course_code 
ON courses(course_code);

EXPLAIN 
SELECT s.first_name, s.last_name, c.course_name 
FROM enrollments e 
JOIN student s ON s.student_id = e.student_id 
JOIN courses c ON c.course_id = e.course_id 
WHERE s.enrollment_year = 2022;

-- The cost after index ranges from 1.14 to 3.40 and exained rows are 11.

CREATE INDEX idx_enrollments_pending_grades 
ON enrollments(student_id) 
WHERE grade IS NULL;
