'''
Print a square of stars recursively (nxn).
'''
def square_star(row_n,column_n):
    if row_n > 0:
        print("*"*column_n)
        square_star(row_n-1,column_n)
try:
    row_num = int(input("Enter number of rows: "))
    column_num = int(input("Enter number of columns: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if row_num <=0 or column_num <= 0:
    print("Invalid! Please enter correct number of stars.")
else:
    square_star(row_num,column_num)