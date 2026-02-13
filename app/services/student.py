from sqlalchemy import select, func
from app.models import Student, Enrollment, Course
from sqlalchemy.orm import Session

def get_students(session: Session):
    return session.scalars(select(Student)).all()

def get_students_with_no_enrollments(session: Session):
    statement = (
        select(Student)
        .outerjoin(Enrollment)
        .where(Enrollment.id.is_(None))
    )

    return session.scalars(statement).all()

def get_student_with_failing_grade(session: Session):
    statement = (
        select(Student)
        .outerjoin(Enrollment)
        .where(Enrollment.grade > 75)
    )

    return session.scalars(statement).all()

def get_student_enrolled_courses(session: Session, student_id):
    statement = (
        select(Student)
        .join(Enrollment)
        .where(Student.id == student_id)
    )

    return session.scalars(statement).first()

# def get_student_enrolled_courses(session: Session, course_id):
#     statement = (
#         select(Student)
#     )

#     return session.scalars(statement).all()