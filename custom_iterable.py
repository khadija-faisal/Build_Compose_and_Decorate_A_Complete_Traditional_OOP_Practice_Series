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





        
