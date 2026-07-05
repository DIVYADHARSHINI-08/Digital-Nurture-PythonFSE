class Student:
    def __init__(self, name):
        self.name = name

class StudentView:
    def display(self, student):
        print(f"Student Name: {student.name}")

class StudentController:
    def __init__(self, student, view):
        self.student = student
        self.view = view

    def update_view(self):
        self.view.display(self.student)


student = Student("Divya")
view = StudentView()
controller = StudentController(student, view)

controller.update_view()