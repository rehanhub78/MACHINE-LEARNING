'''
Given marks of students, find how many passed (>= 40).
'''
marks = [35, 42, 67, 29, 50, 38, 90, 45, 33, 41]
passed = 0
for mark in marks:
    if mark >= 40:
        passed += 1
print(f"Number of students who passed: {passed}")