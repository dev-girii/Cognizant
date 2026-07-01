select * from student where enrollment_year=2022 order by last_name;

select * from courses where credits>=3 order by credits DESC;

select * from professors where salary Between 80000 AND 95000;

select * from student where email like '%@college.edu';

select Count(student_id) as Members, enrollment_year from student group by enrollment_year; 

