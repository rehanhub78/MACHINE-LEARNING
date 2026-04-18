'''
 Print the product of digits of a given number.
'''
try:
    n = int(input("enter a number: "))
    n = abs(n)
    digits = [int(d) for d in str(n)]
    product = 1
    for i in digits:
        if i != 0:
            product *= i

    print(product)
except ValueError:
    print("Invalid! Please enter a numeric digit.")