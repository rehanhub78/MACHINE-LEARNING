'''
Calculate the sum of first n odd numbers recursively. 
'''
def sum_odd(n):
    if n ==0:
        return 0
    else:
        return (2*n - 1) + sum_odd(n-1)
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num < 0:
    print("Invalid! Please enter a non-negative integer.")
else:
    print(f"Sum of first {num} odd numbers is: {sum_odd(num)}")