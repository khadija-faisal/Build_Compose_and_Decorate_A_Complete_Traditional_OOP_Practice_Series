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

