#practice question 6
#6. Constructors and Destructor 

class Logger:
    def __init__(self):
        print("(constructor)")
    def __del__(self):
        print("(destructor)")

# logger = Logger()