from sqlalchemy import select, func
from app.models import Professor
from sqlalchemy.orm import Session

def get_professors(session: Session):
    return session.scalars(select(Professor)).all()