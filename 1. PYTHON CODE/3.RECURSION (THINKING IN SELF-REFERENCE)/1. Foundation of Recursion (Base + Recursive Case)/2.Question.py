'''
Print numbers from n down to 1 using recursion.
'''
def num(n):
    if n > 0:
        print(n,end=" ")
        num(n-1)

num(25)