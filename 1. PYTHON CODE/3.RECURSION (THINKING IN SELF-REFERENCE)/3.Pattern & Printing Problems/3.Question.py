'''
Print a triangle of stars recursively (top-down).
'''
def top_down_star(n,new_n=1):
    if n > 0:
        print("*"*new_n)
        top_down_star(n-1,new_n+1)
try:
    num = int(input("Enter number of rows: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num <=0:
    print("Invalid! Please enter correct number of stars.")
else:
    top_down_star(num)