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