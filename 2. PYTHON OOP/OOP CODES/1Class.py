class Student:
    # Default constructors
    def __init__(self):
        pass
    # parameterized constructors
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("creating new Class")

s1 = Student("karan",97)
print(s1.name,s1.marks)
s2 = Student("arjun",34)
print(s2.name,s2.marks)
