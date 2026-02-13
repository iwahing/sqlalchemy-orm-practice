# Professor

# - id (PK)
# - first_name
# - last_name
# - email (unique)
# - department

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship
from app.database import Base

from email_validator import validate_email, EmailNotValidError

from app.models.course import Course

class Professor(Base):
    __tablename__ = "professors"

    id: Mapped[int] = mapped_column(primary_key=True) 
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    department: Mapped[str] = mapped_column(String(100))
    
    course: Mapped[list["Course"]] = relationship(back_populates="professor")
    
    @validates("email")
    def validate_email(self, _, address):
        try:
            valid = validate_email(address)
            return valid.email
        except EmailNotValidError as e:
            raise ValueError(str(e))
        
    def __repr__(self):
        return f"\nProfessor: [{self.id}] {self.first_name} - {self.department}"