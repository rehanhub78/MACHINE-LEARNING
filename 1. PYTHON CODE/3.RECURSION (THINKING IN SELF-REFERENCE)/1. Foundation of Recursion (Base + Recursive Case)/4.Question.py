'''
Print only odd numbers from 1 to n recursively.
'''
def num(n):
    if n > 0:
        num(n-1)
        if n % 2 != 0:
            print(n, end=" ")

num(100)
