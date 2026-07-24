from app import db


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    head_of_dept = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.Numeric(12, 2), nullable=False)

    courses = db.relationship('Course', back_populates='department', cascade='all, delete-orphan')
    students = db.relationship('Student', back_populates='department', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'head_of_dept': self.head_of_dept,
            'budget': str(self.budget) if self.budget is not None else None,
        }


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    department = db.relationship('Department', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'credits': self.credits,
            'department_id': self.department_id,
        }


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    enrollment_year = db.Column(db.Integer, nullable=False)

    department = db.relationship('Department', back_populates='students')
    enrollments = db.relationship('Enrollment', back_populates='student', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'department_id': self.department_id,
            'enrollment_year': self.enrollment_year,
        }


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    __table_args__ = (
        db.UniqueConstraint('student_id', 'course_id', name='uq_enrollment_student_course'),
    )

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)
    grade = db.Column(db.String(5), nullable=True)

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'enrollment_date': self.enrollment_date.isoformat() if self.enrollment_date else None,
            'grade': self.grade,
        }