# Methods that don't use the self parameter (work at class level)\
class Student:
    @staticmethod  #Decorator
    def hello():
        print("HELLO")

s1 = Student
s1.hello()