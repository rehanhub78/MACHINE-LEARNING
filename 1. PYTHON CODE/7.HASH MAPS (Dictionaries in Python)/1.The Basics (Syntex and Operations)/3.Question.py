'''
write a function to check if a specific key exists in given dictionary without using a try-except block.
'''
student = {}
student["rehan"] = 72
student["alex"] = 98
student["luise"] = 52
def key_checker(dictionary,key):
    return key in dictionary

print(key_checker(student,"alex"))
print(key_checker(student,"bheem"))
