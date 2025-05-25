
#practice question 8
#8. The super() Function:
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher1 = Teacher("Zahid Hussain", "English")
print(f"teacher name: {teacher1.name}")
print(f"teacher subject: {teacher1.subject}")
