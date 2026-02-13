from sqlalchemy import select, func
from app.models import Enrollment
from sqlalchemy.orm import Session

def get_enrollments(session: Session):
    return session.scalars(select(Enrollment)).all()