# Course

# - id (PK)
# - name
# - code (unique)
# - credits
# - professor_id (FK → Professor)

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True) 
    name: Mapped[str] = mapped_column(String(50))
    code: Mapped[str] = mapped_column(String(50), unique=True)
    credits: Mapped[int] = mapped_column()
    
    professor_id: Mapped[int] = mapped_column(ForeignKey("professors.id"))
    professor: Mapped[list["Professor"]] = relationship(back_populates="course")
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="course",cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"\nCourse: [{self.id}] {self.name} by {self.professor_id} : {self.professor} \n" # \n Enrollment : {self.enrollments}