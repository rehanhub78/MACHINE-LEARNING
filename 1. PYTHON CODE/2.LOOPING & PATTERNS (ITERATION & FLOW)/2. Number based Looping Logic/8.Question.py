'''
Print Fibonacci series up to n terms. 
'''
try:
    n = int(input("Enter your number: "))
    a = 0
    b = 1
    if n <= 0 :
        print("Invalid! Please enter a non-zero positive number.")
    else:
        for i in range(n):
            print(a , end=" ")
            a, b = b , a+b
    print()
except ValueError:
    print("Invalid! Please enter numeric digits.")

