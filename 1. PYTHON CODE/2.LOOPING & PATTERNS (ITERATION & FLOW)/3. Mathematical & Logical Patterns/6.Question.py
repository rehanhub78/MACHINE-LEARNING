'''
 Find the sum of all factors of a number.
'''
try:
    num1 = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
if num1 == 0 :
    print("All numbers are factors of 0.")
else:
    n = abs(num1)
    factor_sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            factor_sum += i
    print(f"The sum of the factors is: {factor_sum}")
    
