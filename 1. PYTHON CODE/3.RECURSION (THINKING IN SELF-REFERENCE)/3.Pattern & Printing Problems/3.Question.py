'''
Print a triangle of stars recursively (top-down).
'''
def top_down_star(n):
    if n > 0:
        top_down_star(n-1)
        print("*"*n)
try:
    num = int(input("Enter number of rows: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num <=0:
    print("Invalid! Please enter correct number of stars.")
else:
    top_down_star(num)