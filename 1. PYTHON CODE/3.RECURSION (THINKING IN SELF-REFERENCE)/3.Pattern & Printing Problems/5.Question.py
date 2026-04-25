'''
Print pattern of numbers recursively (1 to n each row).
'''
def num_pattern(n):
    if n > 0:
        num_pattern(n-1)
        for i in range(1,n+1):
            print(i,end="")
        print()
try:
    num = int(input("Enter number of rows: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num <=0:
    print("Invalid! Please enter correct number of stars.")
else:
    num_pattern(num)
