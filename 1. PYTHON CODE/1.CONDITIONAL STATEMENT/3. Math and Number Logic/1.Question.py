'''
Take a 3-digit number and check if all digits are distinct.
'''
a = input("Enter a three digit number: ")
if a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
    print("All digits are not distinct")
else:
    print("All digits are distinct")