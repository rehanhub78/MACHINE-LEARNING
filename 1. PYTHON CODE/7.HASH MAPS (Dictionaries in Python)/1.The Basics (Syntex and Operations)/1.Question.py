'''
Create a dictionary of student names and grades, then write code to add a new student, update a grade, and delete a student.
'''
Student = {}

Student["rehan"] = 72
Student["alex"] = 98
Student["luise"] = 52
print(Student)#print after adding new student

Student["alex"] = 92
print(Student) # print after update

del Student["rehan"]
print(Student)# print after deleting a student
