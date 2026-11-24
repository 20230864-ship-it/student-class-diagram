class Student:
    def __init__(self, student_id: str, full_name: str, program: str) -> None:
        self.__student_id = student_id
        self.__full_name = full_name
        self.__program = program
        self.__course_codes: list[str] = []
        self.__gpa = 0.0

    def enroll(self, course_code: str) -> bool:
        code = course_code.strip().upper()
        if not code or code in self.__course_codes:
            return False

        self.__course_codes.append(code)
        return True

    def withdraw(self, course_code: str) -> bool:
        code = course_code.strip().upper()
        if code not in self.__course_codes:
            return False

        self.__course_codes.remove(code)
        return True

    def update_gpa(self, gpa: float) -> None:
        if not 0.0 <= gpa <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0.")

        self.__gpa = gpa

    def qualifies_for_honors(self) -> bool:
        return self.__gpa >= 3.5

    def summary(self) -> str:
        courses = ", ".join(self.__course_codes) or "None"
        honors = "Yes" if self.qualifies_for_honors() else "No"

        return (
            f"{self.__full_name} ({self.__student_id})\n"
            f"Program: {self.__program}\n"
            f"GPA: {self.__gpa:.2f}\n"
            f"Courses: {courses}\n"
            f"Honors: {honors}"
        )


if __name__ == "__main__":
    student_id = "YOUR_STUDENT_ID"
    student = Student(student_id, "Deniz Kaya", "Computer Engineering")

    student.enroll("CSE101")
    student.enroll("MAT102")
    student.update_gpa(3.65)
    print(student.summary())

    student.withdraw("MAT102")
    print("\nAfter withdrawal")
    print(student.summary())
