from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models import Course, Enrollment
from sqlalchemy.orm import Session

def get_courses(session: Session):
    return session.scalars(select(Course)).all()

def get_courses_students(session: Session):
    statement = (
        select(Course)
        .options(
            selectinload(Course.enrollments)
            .selectinload(Enrollment.student)
        )
    )
    
    return session.scalars(statement).unique().all()