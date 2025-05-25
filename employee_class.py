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
