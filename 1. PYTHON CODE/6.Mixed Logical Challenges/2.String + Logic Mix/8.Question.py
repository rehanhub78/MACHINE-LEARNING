'''
Check if two strings are rotations of each other. 
'''
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if len(s1) != len(s2):
    print("The strings are not rotations of each other.")
else:
    # Concatenate s1 with itself
    s1s1 = s1 + s1
    # Check if s2 is a substring of s1s1
    if s2 in s1s1:
        print("The strings are rotations of each other.")
    else:
        print("The strings are not rotations of each other.")