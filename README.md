# student-class-diagram
Student Name: Muhammed Yuşa okuyucu

Student ID:20230864

Departmant: Sofware engineering
# Student Class — UML to Python

This software engineering assignment maps a Student UML class diagram to Python. The `Student` class supports course enrollment, course withdrawal, GPA updates, and a student profile summary.

## UML Class Diagram



## UML to Python Mapping

| UML element | Python implementation |
| --- | --- |
| `Student(studentId, fullName, program)` | `__init__(student_id, full_name, program)` |
| Private student information | `__student_id`, `__full_name`, `__program` |
| Course list and GPA | `__course_codes: list[str]`, `__gpa: float` |
| `enroll(courseCode)` | `enroll(course_code)` adds a course and prevents duplicates. |
| `withdraw(courseCode)` | `withdraw(course_code)` removes an enrolled course. |
| `updateGpa(gpa)` | `update_gpa(gpa)` accepts GPA values from 0.0 to 4.0. |
| `qualifiesForHonors()` | `qualifies_for_honors()` returns `True` when the GPA is at least 3.5. |
| `summary()` | `summary()` returns the formatted student profile. |

## How to Run

Use Python 3.9 or later. No additional packages are required.

```bash
python student.py
```

The demo enrolls a student in two courses, updates the GPA, and shows the profile before and after withdrawing from one course.

