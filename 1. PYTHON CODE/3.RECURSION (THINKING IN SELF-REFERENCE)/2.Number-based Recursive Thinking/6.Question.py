'''
Convert a number to binary recursively.
'''
def binary_num(n,binary = ""):
    if n == 0:
        return binary
    else:
        new_binary = str(n % 2) + binary 
        return binary_num(n//2,new_binary)
    
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num == 0:
    print(f"Binary of {num} is: 0")
elif num < 0:
    print(f"Binary of {num} is: -{binary_num(abs(num))}")
else:
    print(f"Binary of {num} is: {binary_num(abs(num))}")