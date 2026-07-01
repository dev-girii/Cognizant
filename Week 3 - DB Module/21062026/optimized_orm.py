# For getting 1000 rows in the normal version it takes 2001 query to get all the rows
# Alternatively, in Optimized ORM using JoinedLoad it takes exactly 1 query to fetch all the rows


import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
# Import the engine and model classes from your models.py file
from models import engine, Department, Student, Course, Enrollment

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("\n--- Step 88: Executing Optimized Eager Loading Query ---")
    
    # 88. Rewrite the query using joinedload to eliminate N+1 round-trips
    optimized_enrollments = (
        session.query(Enrollment)
        .options(
            joinedload(Enrollment.student), 
            joinedload(Enrollment.course)
        )
        .all()
    )
    
    print("\n--- Processing Results (Observe that NO extra SQL logs appear below) ---")
    for enroll in optimized_enrollments:
        print(f"Enrollment -> Student: {enroll.student.first_name}, Course: {enroll.course.course_name}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    session.rollback()
finally:
    session.close()