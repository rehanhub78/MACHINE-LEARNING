'''
Find nth Fibonacci number recursively.
'''
def fibonacci(n ,a = 0,b = 1,total = 0,):
    if n >=0:
        print(total)
        fibonacci(n-1, a=b,b = a+b,total = a)
print(fibonacci(5))