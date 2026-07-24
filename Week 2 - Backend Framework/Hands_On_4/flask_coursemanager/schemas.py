from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    code: str
    credits: int
    department_id: int


class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    courses: list[CourseResponse] = Field(default_factory=list)


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    department_id: int
    enrollment_year: int


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    department_id: Optional[int] = None
    enrollment_year: Optional[int] = None


class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: str
    department_id: int
    enrollment_year: int


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: date
    grade: Optional[str] = None


class EnrollmentUpdate(BaseModel):
    student_id: Optional[int] = None
    course_id: Optional[int] = None
    enrollment_date: Optional[date] = None
    grade: Optional[str] = None


class EnrollmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    student_id: int
    course_id: int
    enrollment_date: date
    grade: Optional[str] = None
