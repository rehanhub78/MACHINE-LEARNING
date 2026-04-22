'''
Calculate power of a number (xⁿ) using recursion.
'''
def power(x,n):
    if n == 0:
        return 1
    elif x == 1 or n == 1:
        return x
    elif n < 0:
        return (1/x)*power(x,n+1)
    else:
        return x*power(x,n-1)
try:
    a = int(input("Enter number: "))
    b = int(input("Enter power: "))
except ValueError:
    exit()
    print("Invalid! Please enter a numeric digits.")
print(f"Power of your number is: {power(a,b)}")