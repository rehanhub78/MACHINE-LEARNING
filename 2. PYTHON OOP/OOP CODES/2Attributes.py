class Student:
    college_name = "ABC College"
    name = "anonymus" #classs attribute
    def __init__(self, name, marks):
        self.name = name #obj attribute
        self.marks = marks
        print("creating new Class")

s1 = Student("karan",97)
print(s1.name,s1.marks)
print(s1.college_name)
print(Student.college_name)
