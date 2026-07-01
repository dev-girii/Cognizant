import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import the engine and model classes from your models.py file
from models import engine, Department, Student, Course, Enrollment

# Open a transaction boundary session manager
Session = sessionmaker(bind=engine)
session = Session()

# Helper function to clear previous data from past runs
def clear_existing_data():
    session.query(Enrollment).delete()
    session.query(Course).delete()
    session.query(Student).delete()
    session.query(Department).delete()
    session.commit()

try:
    print("\n--- Clearing past test records ---")
    clear_existing_data()

    # ============================================================================
    # 81. Step 81: INSERT 3 Departments and 5 Students
    # ============================================================================
    print("\n--- Step 81: Inserting Departments and Students ---")
    
    cs_dept = Department(dept_name="Computer Science", hod_name="Dr. Alan Turing", budget=95000.00)
    math_dept = Department(dept_name="Mathematics", hod_name="Dr. Ada Lovelace", budget=60000.00)
    ee_dept = Department(dept_name="Electrical Engineering", hod_name="Dr. Nikola Tesla", budget=80000.00)
    session.add_all([cs_dept, math_dept, ee_dept])
    session.flush() # Flushes data to database to generate structural primary IDs

    s1 = Student(first_name="John", last_name="Doe", email="john.doe@email.com", enrollment_year=2021, department=cs_dept)
    s2 = Student(first_name="Jane", last_name="Smith", email="jane.smith@email.com", enrollment_year=2022, department=cs_dept)
    s3 = Student(first_name="Alice", last_name="Jones", email="alice.j@email.com", enrollment_year=2022, department=math_dept)
    s4 = Student(first_name="Bob", last_name="Miller", email="bob.m@email.com", enrollment_year=2023, department=ee_dept)
    s5 = Student(first_name="Charlie", last_name="Brown", email="charlie.b@email.com", enrollment_year=2023, department=cs_dept)
    session.add_all([s1, s2, s3, s4, s5])
    session.commit()

    # ============================================================================
    # 82. Step 82: INSERT 3 Courses and 4 Enrollments
    # ============================================================================
    print("\n--- Step 82: Inserting Courses and Enrollments ---")
    
    c1 = Course(course_name="Introduction to Python", course_code="CS101", credits=4, department=cs_dept)
    c2 = Course(course_name="Data Structures", course_code="CS102", credits=4, department=cs_dept)
    c3 = Course(course_name="Calculus I", course_code="MATH201", credits=3, department=math_dept)
    session.add_all([c1, c2, c3])
    session.flush()

    e1 = Enrollment(student=s1, course=c1, enrollment_date=datetime.date.today(), grade="A")
    e2 = Enrollment(student=s2, course=c1, enrollment_date=datetime.date.today(), grade="B")
    e3 = Enrollment(student=s3, course=c3, enrollment_date=datetime.date.today(), grade="A")
    e4 = Enrollment(student=s5, course=c2, enrollment_date=datetime.date.today(), grade="C")
    session.add_all([e1, e2, e3, e4])
    session.commit()

    # ============================================================================
    # 83. Step 83: READ Students in 'Computer Science'
    # ============================================================================
    print("\n--- Step 83: Querying Computer Science Students ---")
    
    cs_students = session.query(Student).join(Department).filter(Department.dept_name == "Computer Science").all()
    for student in cs_students:
        print(f"CS Student Found: {student.first_name} {student.last_name}")

    # ============================================================================
    # 84. Step 84: READ All Enrollments (N+1 Query Detection Mode)
    # ============================================================================
    print("\n--- Step 84: Querying All Enrollments ---")
    
    all_enrollments = session.query(Enrollment).all()
    
    # Watch your terminal log carefully as this loop runs!
    for enroll in all_enrollments:
        print(f"Enrollment Record -> Student: {enroll.student.first_name}, Course: {enroll.course.course_name}, Grade: {enroll.grade}")

    # ============================================================================
    # 85. Step 85: UPDATE Student Enrollment Year via Email Lookup
    # ============================================================================
    print("\n--- Step 85: Updating Student Record ---")
    
    target_student = session.query(Student).filter(Student.email == "john.doe@email.com").first()
    if target_student:
        target_student.enrollment_year = 2024
        session.commit()
        print(f"Successfully updated John Doe's enrollment year to: {target_student.enrollment_year}")

    # ============================================================================
    # 86. Step 86: DELETE an Enrollment Record
    # ============================================================================
    print("\n--- Step 86: Deleting an Enrollment Record ---")
    
    enrollment_to_delete = session.query(Enrollment).filter(Enrollment.grade == "C").first()
    if enrollment_to_delete:
        session.delete(enrollment_to_delete)
        session.commit()
        print("Successfully deleted enrollment record with grade 'C'.")
        
    # Verification check to confirm deletion
    remaining_count = session.query(Enrollment).count()
    print(f"Total enrollment records remaining in database: {remaining_count}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    session.rollback()
finally:
    session.close()
