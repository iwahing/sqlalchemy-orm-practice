# Student
# - id (PK)
# - first_name
# - last_name
# - email (unique)
# - date_of_birth
# - enrollment_date

from sqlalchemy import String, Date, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship
from email_validator import validate_email, EmailNotValidError
from datetime import datetime, date

from app.database import Base

class Student(Base):
    __tablename__ = "students"

    # Possibility
    # from sqlalchemy.orm import Column
    # id = mapped_column(Integer, primary_key=True)
    
    id: Mapped[int] = mapped_column(primary_key=True) 
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    date_of_birth: Mapped[date] = mapped_column(Date(), nullable=True)
    
    enrollment_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    enrollments: Mapped[list["Enrollment"]] = relationship(
                                                back_populates="student",
                                                cascade="all, delete-orphan"
                                            )
    
    @validates("email")
    def validate_email(self, _, address):
        try:
            valid = validate_email(address)
            return valid.email
        except EmailNotValidError as e:
            raise ValueError(str(e))
        
    def __repr__(self):
        return f"User: [{self.id}] {self.first_name} {self.last_name}"