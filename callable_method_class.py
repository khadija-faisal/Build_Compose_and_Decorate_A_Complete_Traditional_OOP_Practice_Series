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