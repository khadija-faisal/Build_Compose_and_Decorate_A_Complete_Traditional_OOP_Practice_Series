

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
