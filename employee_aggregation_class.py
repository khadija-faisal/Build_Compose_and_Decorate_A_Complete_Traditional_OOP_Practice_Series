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