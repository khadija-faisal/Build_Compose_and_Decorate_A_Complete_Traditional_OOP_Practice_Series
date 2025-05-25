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


