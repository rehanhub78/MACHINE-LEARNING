'''
Print sum of series 1 + 2 + 3 + ... + n recursively and display each step.
'''
def sum_num(n):
    if n == 0:
        return 0
    else:
        current_sum = n + sum_num(n-1)
        print(f"Step {n}: Adding {n} -> Currnt Total = {current_sum}")
        return current_sum
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num < 0:
    print("Invalid! Please enter a non-negative integer.")
else:
    print(f"Sum of first {num} numbers is: {sum_num(num)}")