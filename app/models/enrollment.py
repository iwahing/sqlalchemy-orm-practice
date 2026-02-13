# Enrollment (Association Table)

# - id (PK)
# - student_id (FK → Student)
# - course_id (FK → Course)
# - enrollment_date
# - grade (nullable, float or string like A/B/C)

from sqlalchemy import Float, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database import Base

class Enrollment(Base):
    __tablename__ = "enrollment"

    id: Mapped[int] = mapped_column(primary_key=True) 
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    enrollment_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    grade: Mapped[float | None] = mapped_column(Float, nullable=True)
    
    student: Mapped[list["Student"]] = relationship(back_populates="enrollments")
    course: Mapped[list["Course"]] = relationship(back_populates="enrollments")
    
    def __repr__(self):
        return f"\nEnrollment: [{self.id}] Student({self.student_id}) - Course({self.course_id}) : Grade {self.grade}"
