alter table student add column phone_number varchar(15);

alter table courses add column max_seats INT DEFAULT 60;

alter table enrollments drop constraint chk_valid_grade;

alter table enrollments add constraint chk_valid_grade check (grade IN ('A', 'B', 'C', 'D', 'F') OR grade is null);

alter table departments rename column hod_name to head_of_dept;

alter table student drop column phone_number;