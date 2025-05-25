#practice question 1
# Using self keyword

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f" Name: {self.name} \n Marks: {self.marks}")


student1 = Student("Wanda", 90)
student2 = Student("Vision", 85)

student1.display()
student2.display()
