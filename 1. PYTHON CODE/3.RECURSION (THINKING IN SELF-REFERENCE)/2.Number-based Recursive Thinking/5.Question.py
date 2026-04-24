'''
Find GCD (HCF) of two numbers using Euclid's algorithm recursively.
'''
def hcf_num(n1,n2):
    if n2 == 0:
        return n1
    else:
        return hcf_num(n2,n1 % n2)
try:
    num1 = int(input("Enter your number 1: "))
    num2 = int(input("Enter your number 2: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()

print(f"The HCF of {num1} and {num2} is: {hcf_num(abs(num1),abs(num2))}")