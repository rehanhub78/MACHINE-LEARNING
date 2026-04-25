'''
Print multiplication table of n recursively.
'''
def table(n,m,i=1):
    if i in range(1,m+1):
        print(f"{n}*{i}={n*i}")
        table(n,m,i+1)

try:
    num = int(input("Enter your number: "))
    steps = int(input("Enter number of steps: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
print(f"The Table of {num} is.")
if steps <= 0:
    print("Plese enter a valid steps.")
else:
    table(num,steps,)
