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