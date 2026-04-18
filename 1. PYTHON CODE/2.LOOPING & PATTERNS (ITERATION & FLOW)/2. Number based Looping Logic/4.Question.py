'''
Find the sum of digits of a number. 
'''
try:
    n = int(input("Enter your number: "))
    num = n
    digit_sum = 0
    if n<0:
        print("Invalid! Please enter a positive number.")
    else:    
        while num > 0:
            last_digit = num % 10
            digit_sum += last_digit
            num = num // 10
        print(f"The sum of digits is {digit_sum}")
except ValueError:
    print("Invalid! Please enter numeric digits.")
