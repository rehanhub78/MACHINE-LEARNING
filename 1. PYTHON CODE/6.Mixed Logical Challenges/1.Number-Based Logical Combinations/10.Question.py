'''
 Check if a number is perfect (sum of factors equals number).
'''
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()
if n < 1:
    print("Please enter a positive integer.")
    exit()
factors_sum = sum(i for i in range(1, n) if n % i == 0)
if factors_sum == n:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")