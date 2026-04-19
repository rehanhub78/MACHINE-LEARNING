'''
Print the squares of numbers from 1 to n.
'''
try:
    n = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
if n<=0:
    print("Invalid! Please enter a non-zero positive number.")
else:
    for i in range(1,n+1):
        print(i**2 , end=" ")

print()
