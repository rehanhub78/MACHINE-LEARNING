'''
Print first n terms of an arithmetic progression (a, d). 
'''
try:
    a = int(input("Enter first term of Arithmetic progression: "))
    d = int(input("Enter difference of Arithmetic progression: "))
    n = int(input("Enter number of terms you want in Arithmetic progression: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()

if n <= 0:
    print("Invalid! Please Enter a positive integer for number of terms.")
else:
    for i in range(0,n):
        print(a + (i*d) , end=" ")
print()
    