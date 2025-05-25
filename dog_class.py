# practice question 10
#10. Instance method

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} is Bark loudly!, because it is {self.breed} ")


dog1 = Dog("holly", "poodle")
dog1.bark()
