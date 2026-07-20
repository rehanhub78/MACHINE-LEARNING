'''
iterate through a dicttionary and print all keys and values in the format: Key: [key], Value: [value]
'''
student = {}

student["rehan"] = 72
student["alex"] = 98
student["luise"] = 52

for key,value in student.items():
    print(f"Key: [{key}], Value: [{value}]")

