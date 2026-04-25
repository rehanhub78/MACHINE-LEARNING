'''
Print reverse triangle pattern recursively.
'''
def rev_triangle(n,y=1):
    if n > 0:
        rev_triangle(n-1,y+1)
        print(" "*(n-1)+"*"*((2*y)-1))

def triangle(n,y=1):
    if n > 0:
        print(" "*(n-1)+"*"*((2*y)-1))
        triangle(n-1,y+1)

try:
    num = int(input("Enter number of rows: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num <=0:
    print("Invalid! Please enter positive number of rows.")
else:
    print("The Triangle pattern is.")
    triangle(num)
    print("The reverse Triangle pattern is.")
    rev_triangle(num)
