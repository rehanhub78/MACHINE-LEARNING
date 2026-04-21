'''
Print numbers from 1 to n using recursion.
'''
def num(n):
    if n > 0:
        num(n-1)
        print(n)

num(100)
