#practice question 15
#15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        return "the show method running 💀"


class B(A):
    def show(self):
        return "the B show method running 💀 "

class C(A):
    def show(self):
        return "the C show method running 💀 "

class D(C, B):
    pass

d = D()
print(d.show())
print(D.mro())
