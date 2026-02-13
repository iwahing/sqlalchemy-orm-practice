from app.database import engine, Base
from app.seed import seed_data
# from app.services import get_students, get_courses, get_enrollments, get_professors
# from app.services import get_students, get_students_with_no_enrollments, get_student_with_failing_grade
# from app.services import get_courses, get_courses_students
from app.services import get_student_enrolled_courses, get_professor
from app.database import SessionLocal

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()

    session = SessionLocal()


    # print("Database initializing ...")
    # seed_data(session)
    # print("Database initialized and seeded.")

    # print("Professors: ")
    # print(get_professors(session))
    prof = get_professor(session, 1)
    for c in prof.course: # type: ignore
        print(c)

    # print(f"Students: \n(\n{get_students(session)}\n)")
    # print(f"Students with no enrollments: \n(\n{get_students_with_no_enrollments(session)}\n)")
    # print(f"Students with failing grade: \n(\n{get_student_with_failing_grade(session)}\n)")
    # print(get_students(session))

    # student = get_student_enrolled_courses(session, 2)
    # for e in student.enrollments: # type: ignore
    #     print(e.course)


    # print(f"Courses Available: \n{get_courses(session)}")
    # print(get_courses(session))
    # courses = get_courses_students(session)

    # for course in courses:
    #     print(f"Course: {course.name}")

    #     students = [e.student for e in course.enrollments]

    #     for student in students:
    #         print(f"   - {student.first_name} {student.last_name}")

    # print("Enrollments: ")
    # print(get_enrollments(session))


    session.close()
