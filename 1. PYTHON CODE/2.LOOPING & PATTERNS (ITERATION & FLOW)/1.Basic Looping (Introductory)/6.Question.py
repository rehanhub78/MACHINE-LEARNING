'''
Print the factorial of a given number. 
'''
try:
    n = int(input("Enter a number: "))
    fact = 1
    if n <= 0:
        print("Enter a positive number")
    else:
        for i in range(1,n+1):
            fact *= i
        print(fact)
except ValueError:
    print("Invalid! Please enter a numeric digit.")