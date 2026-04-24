'''
Find product of digits of a number recursively.
'''
def digits_product(n,product=1):
    if n==0:
        return product
    else:
        last_digit = n % 10
        new_product = product*last_digit
        return digits_product(n // 10, new_product)
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num==0:
    print(f"Product of digits of {num} is: 0")
else:
    print(f"Product of digits of {num} is: {digits_product(abs(num))}")     