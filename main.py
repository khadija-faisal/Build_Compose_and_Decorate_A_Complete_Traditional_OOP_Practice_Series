# I create a separate file for each question also i add all questions in main.py 




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








# practice question 2
#2. Using cls

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def display(cls):
       
        print(f"the number of objects created: {cls.count}")

obj1 = Counter()
obj2 = Counter()
Counter.display()




#practice question 3
#3. Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"The {self.brand} is starting.........")


car1 = Car("BMW")
car2 = Car("Mercedes")

print(car1.brand)
car1.start()

print(car2.brand)
car2.start()


#practice question 4
# 4. Class Variables and Class Methods

class Bank:
    bank_name = "UBL"
    def __init__(self):
        pass
    @classmethod
    def change_bank_name(cls, new_name):
         cls.bank_name = new_name
         print(f"Bank name changed to {cls.bank_name}")

branch1 = Bank() #UBL
branch2 = Bank() #UBL

print(branch1.bank_name)
print(branch2.bank_name)

Bank.change_bank_name("HBL")

# change for all instances
print(branch1.bank_name)
print(branch2.bank_name)






#practice question 5
#5. Static Variables and Static 
class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b

print(MathUtils.add(10,20))





#practice question 6
#6. Constructors and Destructor 

class Logger:
    def __init__(self):
        print("(constructor)")
    def __del__(self):
        print("(destructor)")

# logger = Logger()



#practice question 7
#7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self.__ssn = "12345"
    
obj1 = Employee("Khadija", "100000000")


#accessing public variable
print(f"Employee Name: {obj1.name} ") #This works fine because public variables are fully accessible outside the class ✅ Allowed.
#accessing protected variable
print(f"Employee Salary: {obj1._salary}") #this will give you output and print protected variable but ⚠️ Discouraged, It's intended for internal use or subclass use,
# Use getter/setter methods or @property decorators to access.

#accessing private variable
#print(f"employee Ssn: {obj1.__ssn}") # currently not accessible or output throw AttributeError, 


# we can access by name name mangling by (_ClassName__var):
print(f"employee _ssn: {obj1._Employee__ssn}") #but not recommended
#Provide controlled access via methods only





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





#practice quesion 9
#9. Abstract Classes and Methods

from abc import ABC, abstractmethod
from typing import Any

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

    

rectangle1 = Rectangle(4,8)
print(f"the total dimension of rectangle is : {rectangle1.area()}cm")



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





#practice question 11
#11. Class Methods
class Book:
    total_books = 5
    @classmethod
    def increment_book_count(cls, count):
        cls.total_books += count


    
Book().increment_book_count(5)
print(f"the count of total books {Book.total_books}")
        



#practice question 12
#12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

output = TemperatureConverter.celsius_to_fahrenheit(30)
print(f"The result of celsius to fahrenheit {output}°F ")

    

#question practice 13
#13. Composition
class Engine:
    def engine_on(self):
        return "brumm brummm......"

class Car:
    def __init__(self):
        self.engine = Engine()
    def engine_on(self):
        return self.engine.engine_on()


car_bmw  = Car()
print(car_bmw.engine_on())




#question practice 14
#14. Aggregation
class Employee:
    def __init__(self, employee_name):
        self.name = employee_name
    
    def get_name(self):
        return f"employee Name {self.name}"

class Department:
    def __init__(self, employee_name, depart_name ):
        self.employee_name = employee_name
        self.depart_name = depart_name
    
    def show_details(self):
        return f"Department {self.depart_name}, {self.employee_name.get_name()}"


employee = Employee("khadijaa")

dpart = Department(employee, "HR")

print(dpart.show_details())

    

#practice question 15
#15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        return "the show method running 💀"


class B(A):
    def show(self):
        return "the B show method running 💀 "

class C(A):
    def show(self):
        return "the C show method running 💀 "

class D(C, B):
    pass

d = D()
print(d.show())
print(D.mro())




#practice question 16
#16. Function Decorators
def log_function_call(func):

    def wrapper():
       print("Function is being called")
       return func()
    return wrapper

@log_function_call
def say_hello():
    print("hello i'm khadijaa")
    
say_hello()


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





#practice question 18
#18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return f"the product price is: {self.__price}$"
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price,(int,float)):
            self.__price = new_price
        else:
            raise ValueError("value must be int or float")

    @price.deleter
    def price(self):
        print("Deleting.....")
        del self.__price


product1 = Product(10.5)
#get product 
# __price which we made by using @property decorator
print(product1.price)
#update __price which we made by using @attribute.setter decorator
product1.price = 100.7
#print updated __price
print(product1.price)
#delete  __price which we made by using @attribute.deleter decorator 
del product1.price # run deleter

#print(product1.price) #throw AttributeError: 'Product' object has no attribute '_Product__price'   




#practice question 19
#19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
       
    def __call__(self, value):
        return self.factor * value



#  Create object with a factor (e.g. 6)
fact1 = Multiplier(6)
#  Check if it's callable
print(callable(fact1))
# Call the object with a value (e.g. 10)
response = fact1(10)   # This does: 6 * 10
print(f"the result of {response}") # Output: Result is: 60



#practice question 20
#20. Creating a Custom Exception

class InvalidAgeError(Exception):
     def __init__(self, age):
         super().__init__(f"Insufficient age, age is : {age} age must be greater then or equal to 18")
         self.age = age
        


def check_age(age):
    try:
        if age >= 18:
            print("you are eligible")
        else: 
            raise InvalidAgeError(age)
    except InvalidAgeError as e:
        print(e)
   
check_age(20)
check_age(17)



    


#practice question 21
#21. Make a Custom Class Iterable


class Countdown:
    def __init__(self, range):
        self.range = range
        self.current = range
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 0:
            value = self.current 
            self.current -= 1
            return value
        else:
            raise StopIteration


count_range = Countdown(10)

for num in count_range:
    print(num)





        
