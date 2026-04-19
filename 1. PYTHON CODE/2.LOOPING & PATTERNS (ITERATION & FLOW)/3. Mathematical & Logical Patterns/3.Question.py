'''
Find HCF (GCD) of two numbers using loops.
'''
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
a = num1
b = num2
if a == 0 or b == 0:
    while b != 0:
        a, b = b , a % b
    print(f"HCF of {num1} and {num2} is: {a}")
elif a>b:
    while a % b != 0:
        a , b = b , a % b
    print(f"HCF of {num1} and {num2} is: {b}")
else:
    while b % a != 0:
        a , b = b % a , a
    print(f"HCF of {num1} and {num2} is: {a}")

#shortest way
while b != 0:
    a, b = b , a % b
    
print(f"HCF of {num1} and {num2} is: {a}")