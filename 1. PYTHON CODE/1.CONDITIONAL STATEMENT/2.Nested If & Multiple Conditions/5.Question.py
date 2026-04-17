'''
Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a%2==0 and b%2==0:
    print("Both are even")
elif a%2!=0 and b%2!=0:
    print("Both are odd")
else:
    print("One is even and One is odd")

