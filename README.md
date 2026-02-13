# Task

## 📦 Requirements

### Database Models

Student

- id (PK)
- first_name
- last_name
- email (unique)
- date_of_birth
- enrollment_date

Professor

- id (PK)
- first_name
- last_name
- email (unique)
- department

Course

- id (PK)
- name
- code (unique)
- credits
- professor_id (FK → Professor)

Enrollment (Association Table)

- id (PK)
- student_id (FK → Student)
- course_id (FK → Course)
- enrollment_date
- grade (nullable, float or string like A/B/C)

### Relationships You Must Implement

One Professor → Many Courses

Many Students ↔ Many Courses (via Enrollment)

Student → Enrollments

Course → Enrollments

Use:

relationship()

back_populates

secondary (if you attempt alternative version)

### 🛠️ Tasks To Complete

Part 1 — Setup

Create SQLite database

Create all tables

Insert:

5 students

3 professors

5 courses

Enroll students in multiple courses

Part 2 — Query Practice

Write ORM queries for:

Get all students enrolled in a specific course

Get all courses a specific student is taking

Get all courses taught by a specific professor

Find students with no enrollments

Calculate average grade per course

Find the top-performing student (highest average grade)

Count how many students each professor teaches

Part 3 — Advanced ORM Practice

Implement:

A hybrid property that calculates:

Student’s average grade

Cascade delete:

If a course is deleted → its enrollments are deleted

Add validation:

No duplicate student enrollments in same course

Add index on:

email

course code

### 🚀 Bonus Challenges

Use Alembic for migrations

Add pagination to queries

Add soft delete to Student model

Create CLI interface for:

Add student

Enroll student

Assign grade

Convert to async SQLAlchemy

Write pytest tests

### 💡 Extra Difficulty Version

Add:

Prerequisites table (course → course relationship)

GPA calculation weighted by credits

Attendance tracking

Semester support

### 📊 Expected Skills Practiced

Declarative models

Relationships

Association tables

Query joins

Aggregation functions (func.avg, func.count)

Hybrid properties

Constraints & indexes

Cascades

Session management

Transaction handling
