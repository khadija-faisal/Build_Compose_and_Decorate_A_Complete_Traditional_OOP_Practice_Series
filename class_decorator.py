#practice question 17
#17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return f"hello from Decorator to, {self.name} "
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
        

p1 = Person("khadija")
print(p1.greet())
