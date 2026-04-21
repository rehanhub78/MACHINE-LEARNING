'''
Print factorial of each number from 1 to n.
'''
try:
    n = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
if n <= 0:
    print("Invalid! Please enter a positive number.")
else:
    for i in range(1,n+1):
        fact = 1
        for j in range(1,i+1):
            fact *= j
        print(fact, end=" ")
    # Shortest way
    print()
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact, end=" ")
print()