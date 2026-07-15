'''
Generate Fibonacci series up to N using recursion.
'''
n = 5
def fibonacci(n):
    if n < 0:
        return []
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(n):    
    print(fibonacci(i), end=' ')

print()