
#practice question 18
#18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return f"the product price is: {self.__price}$"
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price,(int,float)):
            self.__price = new_price
        else:
            raise ValueError("value must be int or float")

    @price.deleter
    def price(self):
        print("Deleting.....")
        del self.__price


product1 = Product(10.5)
#get product 
# __price which we made by using @property decorator
print(product1.price)
#update __price which we made by using @attribute.setter decorator
product1.price = 100.7
#print updated __price
print(product1.price)
#delete  __price which we made by using @attribute.deleter decorator 
del product1.price # run deleter

#print(product1.price) #throw AttributeError: 'Product' object has no attribute '_Product__price'   
