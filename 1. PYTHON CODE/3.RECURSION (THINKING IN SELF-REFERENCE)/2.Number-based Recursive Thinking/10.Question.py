'''
Find nCr (Combination formula) recursively using Pascal's relation.
'''
def nCr(n,r):
    if r==0 or n == r:
        return 1
    else:
        return nCr(n-1,r-1) + nCr(n-1,r)
    
try:
    num = int(input("Enter Total number of items: "))
    r_num = int(input("Enter number of items to choose: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num < 0 or r_num < 0 or r_num > num:
    print("Invalid! Please enter valid values.")
else:
    print(f"nCr = {nCr(num, r_num)}")