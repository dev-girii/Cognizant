from decimal import Decimal, InvalidOperation

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from app import db
from courses.models import Course, Department, Enrollment, Student


courses_bp = Blueprint('courses', __name__)


def _parse_decimal(value):
    if value is None:
        return None

    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return None


@courses_bp.route('/', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


@courses_bp.route('/', methods=['POST'])
def create_course():
    payload = request.get_json(silent=True) or {}

    if not all(key in payload for key in ('name', 'code', 'credits', 'department_id')):
        return jsonify(error='Missing required course fields'), 400

    department = Department.query.get_or_404(payload['department_id'])
    course = Course(
        name=payload['name'],
        code=payload['code'],
        credits=payload['credits'],
        department=department,
    )

    db.session.add(course)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(error='Course code already exists or payload is invalid'), 409

    return jsonify(course.to_dict()), 201


@courses_bp.route('/<int:id>/', methods=['GET'])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())


@courses_bp.route('/<int:id>/', methods=['PUT'])
def update_course(id):
    course = Course.query.get_or_404(id)
    payload = request.get_json(silent=True) or {}

    if 'department_id' in payload:
        course.department = Department.query.get_or_404(payload['department_id'])

    if 'name' in payload:
        course.name = payload['name']
    if 'code' in payload:
        course.code = payload['code']
    if 'credits' in payload:
        course.credits = payload['credits']

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(error='Course code already exists or payload is invalid'), 409

    return jsonify(course.to_dict())


@courses_bp.route('/<int:id>/', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return '', 204


@courses_bp.route('/<int:id>/students/', methods=['GET'])
def course_students(id):
    course = Course.query.get_or_404(id)
    students = (
        db.session.execute(
            db.select(Student)
            .join(Enrollment)
            .where(Enrollment.course_id == course.id)
            .distinct()
        )
        .scalars()
        .all()
    )

    return jsonify([student.to_dict() for student in students])