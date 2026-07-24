from datetime import date
from typing import AsyncGenerator, Optional

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, status
from sqlalchemy import ForeignKey, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload

from schemas import (
    CourseCreate,
    CourseResponse,
    CourseUpdate,
    DepartmentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
    EnrollmentUpdate,
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)

DATABASE_URL = "sqlite+aiosqlite:///./coursemanager.db"

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    courses: Mapped[list["Course"]] = relationship(back_populates="department", lazy="selectin")
    students: Mapped[list["Student"]] = relationship(back_populates="department", lazy="selectin")


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    credits: Mapped[int] = mapped_column(nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=False)
    department: Mapped[Department] = relationship(back_populates="courses")
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="course", lazy="selectin", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=False)
    enrollment_year: Mapped[int] = mapped_column(nullable=False)

    department: Mapped[Department] = relationship(back_populates="students")
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="student", lazy="selectin", cascade="all, delete-orphan")


class Enrollment(Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    enrollment_date: Mapped[date] = mapped_column(nullable=False)
    grade: Mapped[Optional[str]] = mapped_column(nullable=True)

    student: Mapped[Student] = relationship(back_populates="enrollments")
    course: Mapped[Course] = relationship(back_populates="enrollments")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


app = FastAPI(
    title="Course Management API",
    description="Async API for managing courses, students, and enrollments.",
    version="1.0",
    contact={"name": "Course API Support", "email": "support@example.com"},
)


@app.on_event("startup")
async def on_startup() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "API running"}


@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a course",
    response_description="The created course",
    tags=["Courses"],
)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)) -> Course:
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@app.get("/api/courses/", response_model=list[CourseResponse], tags=["Courses"])
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
) -> list[Course]:
    statement = select(Course).offset(skip).limit(limit)
    if department_id is not None:
        statement = statement.where(Course.department_id == department_id)

    result = await db.execute(statement)
    return list(result.scalars().all())


@app.get("/api/courses/{course_id}", response_model=CourseResponse, tags=["Courses"])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)) -> Course:
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course


@app.put("/api/courses/{course_id}", response_model=CourseResponse, tags=["Courses"])
async def update_course(
    course_id: int,
    course_update: CourseUpdate,
    db: AsyncSession = Depends(get_db),
) -> Course:
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    update_data = course_update.model_dump(exclude_unset=True)
    for field_name, value in update_data.items():
        setattr(course, field_name, value)

    await db.commit()
    await db.refresh(course)
    return course


@app.delete("/api/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Courses"])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)) -> None:
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    await db.delete(course)
    await db.commit()


@app.get("/api/courses/{course_id}/students/", response_model=list[StudentResponse], tags=["Courses"])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)) -> list[Student]:
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    statement = (
        select(Student)
        .join(Enrollment)
        .where(Enrollment.course_id == course_id)
        .distinct()
    )
    result = await db.execute(statement)
    return list(result.scalars().all())


@app.post("/api/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=["Students"])
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)) -> Student:
    department = await db.get(Department, student.department_id)
    if department is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")

    new_student = Student(**student.model_dump())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student


@app.get("/api/students/", response_model=list[StudentResponse], tags=["Students"])
async def get_students(db: AsyncSession = Depends(get_db)) -> list[Student]:
    result = await db.execute(select(Student))
    return list(result.scalars().all())


@app.get("/api/students/{student_id}", response_model=StudentResponse, tags=["Students"])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)) -> Student:
    student = await db.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student


@app.put("/api/students/{student_id}", response_model=StudentResponse, tags=["Students"])
async def update_student(student_id: int, student_update: StudentUpdate, db: AsyncSession = Depends(get_db)) -> Student:
    student = await db.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    update_data = student_update.model_dump(exclude_unset=True)
    for field_name, value in update_data.items():
        setattr(student, field_name, value)

    await db.commit()
    await db.refresh(student)
    return student


@app.delete("/api/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Students"])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)) -> None:
    student = await db.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    await db.delete(student)
    await db.commit()


def send_confirmation_email(student_email: str) -> None:
    print(f"Sending confirmation to {student_email}")


@app.post("/api/enrollments/", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=["Enrollments"])
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
) -> Enrollment:
    student = await db.get(Student, enrollment.student_id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    course = await db.get(Course, enrollment.course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        enrollment_date=enrollment.enrollment_date,
        grade=enrollment.grade,
    )
    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    background_tasks.add_task(send_confirmation_email, student.email)
    return new_enrollment


@app.get("/api/enrollments/", response_model=list[EnrollmentResponse], tags=["Enrollments"])
async def get_enrollments(db: AsyncSession = Depends(get_db)) -> list[Enrollment]:
    result = await db.execute(select(Enrollment))
    return list(result.scalars().all())


@app.get("/api/enrollments/{enrollment_id}", response_model=EnrollmentResponse, tags=["Enrollments"])
async def get_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)) -> Enrollment:
    enrollment = await db.get(Enrollment, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")
    return enrollment


@app.put("/api/enrollments/{enrollment_id}", response_model=EnrollmentResponse, tags=["Enrollments"])
async def update_enrollment(
    enrollment_id: int,
    enrollment_update: EnrollmentUpdate,
    db: AsyncSession = Depends(get_db),
) -> Enrollment:
    enrollment = await db.get(Enrollment, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")

    update_data = enrollment_update.model_dump(exclude_unset=True)
    if "student_id" in update_data:
        student = await db.get(Student, update_data["student_id"])
        if student is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    if "course_id" in update_data:
        course = await db.get(Course, update_data["course_id"])
        if course is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    for field_name, value in update_data.items():
        setattr(enrollment, field_name, value)

    await db.commit()
    await db.refresh(enrollment)
    return enrollment


@app.delete("/api/enrollments/{enrollment_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Enrollments"])
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)) -> None:
    enrollment = await db.get(Enrollment, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")

    await db.delete(enrollment)
    await db.commit()


@app.get("/api/departments/{department_id}", response_model=DepartmentResponse, tags=["Departments"])
async def get_department(department_id: int, db: AsyncSession = Depends(get_db)) -> Department:
    statement = select(Department).options(selectinload(Department.courses)).where(Department.id == department_id)
    result = await db.execute(statement)
    department = result.scalar_one_or_none()
    if department is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
    return department
