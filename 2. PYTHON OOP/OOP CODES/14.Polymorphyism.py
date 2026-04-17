# Polymorphism : Operator Overloading
        # When the same operator is allowed to have diffrent meaning according to the context.
class Complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2): # Add dunder function
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
    
    def __sub__(self, num2): # sub dunder function
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal, newimg)
# For more Dunder function you can go on "docs.python.org" in 3.3.8. part.

num1 = Complex(1, 3)
num1.shownumber()

num2 = Complex(4, 6)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

num3 = num1 - num2
num3.shownumber()