# Methods are functons that belong to objects
class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks


    def welcome(self):
        print("welcome student,", self.name)


s1= Student("karan",97)
s1.welcome()