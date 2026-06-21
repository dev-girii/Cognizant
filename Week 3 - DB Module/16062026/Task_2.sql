select course_id, course_name FROM courses WHERE course_name Like '%%';

select email, count(*) from student GROUP BY email HAVING count(*)>1;


select student_id, course_id, count(DISTINCT grade) from enrollments group by student_id, course_id HAVING count(DISTINCT grade)>1;

select department_id, salary, count(*) from professors group by department_id, salary having count(*)>1;