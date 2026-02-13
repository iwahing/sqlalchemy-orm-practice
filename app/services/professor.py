from sqlalchemy import select, func
from app.models import Professor, Course
from sqlalchemy.orm import Session

def get_professors(session: Session):
    return session.scalars(select(Professor)).all()

def get_professor(session: Session, professor_id):
    statement = (
        select(Professor)
        .join(Course)
        .where(Professor.id == professor_id)
    )

    return session.scalars(statement).first()