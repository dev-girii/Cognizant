CREATE TABLE IF NOT EXISTS department_transfer_log (
    log_id SERIAL PRIMARY KEY,
    student_id INT,
    old_department_id INT,
    new_department_id INT,
    transfer_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION fn_enroll_student(p_student_id INT, p_course_id INT, p_enrollment_date DATE) 
RETURNS VOID AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM enrollments WHERE student_id = p_student_id AND course_id = p_course_id) THEN
        RAISE EXCEPTION 'Duplicate Enrollment Error';
    END IF;
    INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (p_student_id, p_course_id, p_enrollment_date);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE sp_transfer_student(p_student_id INT, p_new_dept_id INT) AS $$
DECLARE v_old_dept_id INT;
BEGIN
    SELECT department_id INTO v_old_dept_id FROM student WHERE student_id = p_student_id;
    UPDATE student SET department_id = p_new_dept_id WHERE student_id = p_student_id;
    INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id) VALUES (p_student_id, v_old_dept_id, p_new_dept_id);
EXCEPTION WHEN OTHERS THEN
    RAISE;
END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN
    DELETE FROM enrollments WHERE student_id = 1;
    INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (1, 1, CURRENT_DATE);
    SAVEPOINT enrollment_checkpoint;
    BEGIN
        INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (1, 999999, CURRENT_DATE);
    EXCEPTION WHEN OTHERS THEN
        ROLLBACK TO SAVEPOINT enrollment_checkpoint;
    END;
END $$;

SELECT * FROM enrollments WHERE student_id = 1;
