'''
Print a line of n stars recursively.
'''
def star_print(n):
    if n >0:
        print("*",end="")
        star_print(n-1)

try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num <=0:
    print("Invalid! Please enter correct number of stars.")
else:
    star_print(num)