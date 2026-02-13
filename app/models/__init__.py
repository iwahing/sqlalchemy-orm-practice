from .student import Student

# from sqlalchemy import String, Date, DateTime
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from datetime import datetime
# from app.database import Base


# class Student(Base):
#     __tablename__ = "students"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     first_name: Mapped[str] = mapped_column(String(50))
#     last_name: Mapped[str] = mapped_column(String(50))
#     email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
#     date_of_birth: Mapped[Date]
#     enrollment_date: Mapped[DateTime] = mapped_column(default=datetime.utcnow)

#     enrollments = relationship(
#         "Enrollment",
#         back_populates="student",
#         cascade="all, delete-orphan"
#     )


from .professor import Professor

# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from app.database import Base


# class Professor(Base):
#     __tablename__ = "professors"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     first_name: Mapped[str] = mapped_column(String(50))
#     last_name: Mapped[str] = mapped_column(String(50))
#     email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
#     department: Mapped[str] = mapped_column(String(100))

#     courses = relationship(
#         "Course",
#         back_populates="professor"
#     )


from .course import Course

# from sqlalchemy import String, Integer, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from app.database import Base


# class Course(Base):
#     __tablename__ = "courses"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     code: Mapped[str] = mapped_column(String(20), unique=True, index=True)
#     credits: Mapped[int] = mapped_column(Integer)

#     professor_id: Mapped[int] = mapped_column(ForeignKey("professors.id"))
#     professor = relationship("Professor", back_populates="courses")

#     enrollments = relationship(
#         "Enrollment",
#         back_populates="course",
#         cascade="all, delete-orphan"
#     )


from .enrollment import Enrollment

# from sqlalchemy import ForeignKey, DateTime, Float, UniqueConstraint
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from datetime import datetime
# from app.database import Base


# class Enrollment(Base):
#     __tablename__ = "enrollments"

#     __table_args__ = (
#         UniqueConstraint("student_id", "course_id", name="unique_enrollment"),
#     )

#     id: Mapped[int] = mapped_column(primary_key=True)

#     student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
#     course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))

#     enrollment_date: Mapped[DateTime] = mapped_column(default=datetime.utcnow)
#     grade: Mapped[float | None] = mapped_column(Float, nullable=True)

#     student = relationship("Student", back_populates="enrollments")
#     course = relationship("Course", back_populates="enrollments")
