'''
Print a triangle of stars recursively (bottom-up).
'''
def bottom_up_star(n):
    if n > 0:
        print("*"*n)
        bottom_up_star(n-1)
try:
    num = int(input("Enter number of rows: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num <=0:
    print("Invalid! Please enter correct number of stars.")
else:
    bottom_up_star(num)