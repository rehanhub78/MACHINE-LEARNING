'''
Calculate the sum of first n even numbers recursively.
'''
def sum_even(n):
    if n ==0:
        return 0
    else:
        return 2 * n + sum_even(n - 1)
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num < 0:
    print("Invalid! Please enter a non-negative integer.")
else:
    print(f"Sum of first {num} even numbers is: {sum_even(num)}")