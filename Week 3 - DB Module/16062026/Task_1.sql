create database college_db;

create table departments(
department_id SERIAL PRIMARY KEY,
dept_name VARCHAR(100) NOT NULL,
hod_name VARCHAR(100),
budget DECIMAL(12,2)
);


create table student(
student_id SERIAL PRIMARY KEY NOT NULL,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
date_of_birth DATE,
department_id INT,
enrollment_year INT,
CONSTRAINT fk_department FOREIGN KEY(department_id) REFERENCES departments(department_id)
);


create table courses(
course_id SERIAL PRIMARY KEY,
course_name VARCHAR(150) NOT NULL,
course_code VARCHAR(20) UNIQUE,
credits INT,
department_id INT,
CONSTRAINT fk_department FOREIGN KEY(department_id) REFERENCES departments(department_id)
);


create table enrollments(
enrollment_id SERIAL PRIMARY KEY,
student_id INT,
course_id INT,
enrollment_date DATE,
grade char(2) constraint chk_valid_grade check(grade IN ('A', 'B' , 'C', 'D', 'F')),
CONSTRAINT fk_course FOREIGN KEY(course_id) REFERENCES courses(course_id),
constraint fk_students FOREIGN KEY(student_id) References student(student_id)
);

create table professors(
professor_id SERIAL PRIMARY KEY,
prof_name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE,
department_id INT,
salary DECIMAL(10,2),
CONSTRAINT fk_department FOREIGN KEY(department_id) REFERENCES departments(department_id)
);
