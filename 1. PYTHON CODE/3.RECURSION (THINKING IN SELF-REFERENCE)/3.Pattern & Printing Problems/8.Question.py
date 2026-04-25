'''
Print numbers in increasing and decreasing order in same function.
'''
def inc_dec(n):
    if n > 0:
        print(n , end=" ")
        inc_dec(n-1)
        print(n , end=" ")

try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num <=0:
    print("Invalid! Please enter positive number.")
else:
    print(f"The sequence for {num} is: ")
    inc_dec(num)
print()