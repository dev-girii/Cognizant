-- This is a query used to verify the 1NF, 2NF and 3NF

-- This query checks for the atomicity and Null values ensuring it is 1NF
select course_id, course_name FROM courses WHERE course_name Like '%%';


-- This query check the Primary key integrity so that ensuring it is 1NF
select email, count(*) from student GROUP BY email HAVING count(*)>1;

-- Checks for the partial dependencies which ensures that it is 2NF
select student_id, course_id, count(DISTINCT grade) from enrollments group by student_id, course_id HAVING count(DISTINCT grade)>1;

-- Checks for the transitive dependencies which ensures that it is 3NF
select department_id, salary, count(*) from professors group by department_id, salary having count(*)>1;