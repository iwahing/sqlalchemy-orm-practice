from sqlalchemy.orm import Session
from app.models import Student, Enrollment, Professor, Course
from datetime import date

def seed_data(session: Session):
    prof1 = Professor(first_name="John", last_name="Smith",
                      email="john@uni.com", department="Computer Science")


    prof4 = Professor(first_name="Jane", last_name="Smith",
                      email="Jane@uni.com", department="Computer Science")


    prof2 = Professor(first_name="Cecilia", last_name="Wahing",
                      email="cywahing@deped.com.ph", department="Education")


    prof3 = Professor(first_name="Wendell", last_name="Wahing",
                      email="wwahing@gmail.com", department="Engineering")

    course1 = Course(name="Databases", code="CS101", credits=3, professor=prof1)
    course2 = Course(name="Algorithms", code="CS102", credits=4, professor=prof1)
    course3 = Course(name="English", code="ENG101", credits=3, professor=prof2)
    course4 = Course(name="Physics", code="PHY101", credits=3, professor=prof3)

    student1 = Student(
        first_name="Alice",
        last_name="Brown",
        email="alice@email.com",
        date_of_birth=date(2000, 5, 12)
    )

    student2 = Student(
        first_name="Isaac",
        last_name="Wahing",
        email="isaacjohnwahing@gmail.com",
        date_of_birth=date(2000, 5, 12)
    )

    student3 = Student(
        first_name="Joanna",
        last_name="Victoria",
        email="jv@gmail.com",
        date_of_birth=date(2000, 5, 12)
    )

    enrollment1 = Enrollment(student=student1, course=course1, grade=90)
    enrollment2 = Enrollment(student=student1, course=course2, grade=75)
    enrollment3 = Enrollment(student=student2, course=course1, grade=81)
    enrollment4 = Enrollment(student=student2, course=course2, grade=88)
    enrollment5 = Enrollment(student=student2, course=course3, grade=93)
    enrollment6 = Enrollment(student=student2, course=course4, grade=95)
    enrollment7 = Enrollment(student=student3, course=course3, grade=95)

    session.add_all([prof1, prof2, prof3, prof4, course1, course2, course3, course4, student1, student2, student3, \
        enrollment1, enrollment2, enrollment3, enrollment4, enrollment5, enrollment6, enrollment7])

    student4 = Student(
        first_name="Jhai",
        last_name="Desabelle",
        email="jhaid@gmail.com",
        date_of_birth=date(2000, 5, 12)
    )

    session.add(student4)
    session.commit()