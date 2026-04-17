'''
Take a 3-digit number and check if the sum of the first and last digit equals the middle digit. 
'''
import math
while True:
    try:
        a = int(input("Enter a three digit number: "))
        if a<100 or a>999:
            print("Invalid! Please enter correct three digit number.")
            continue
        digits = [int(d) for d in str(a)]
        digit_sum = digits[0]  + digits[2]
        if digit_sum == digits[1]:
            print(f"The sum of the first and last digit equals the middle digit of enter number: {a}.")
            break
        else:
            print(f"The sum of the first and last digit is not equals the middle digit of enter number: {a}.")

    except ValueError:
        print("Invalid input! Please enter numeric digit.")
