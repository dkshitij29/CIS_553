class Course:
    def __init__(self, course_id, name, price):
        self.course_id = course_id
        self.name = name
        self.price = price
        self.enrolled_students = []

    def enroll(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"{student.name} enrolled in {self.name}")

    def drop(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"{student.name} dropped {self.name}")

    def revenue(self):
        return len(self.enrolled_students) * self.price
