'''
Print Fibonacci series up to n terms recursively.
'''
def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)
try:
    terms = int(input("Enter how many terms you want: "))
except ValueError:
    print("Invalid! Please enter a numeric digits.")
    exit()
if terms<=0:
    print("Invalid! Please enter a positive number.")
else:
    print(f"The Fibonacci series up to {terms} terms is: ")
    for i in range(terms):
        print(get_fibonacci(i), end=" ")

    print()
