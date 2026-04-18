'''
Check if a number is an Armstrong number.
'''
try:
    n = int(input("Enter your number: "))
    num = n
    armstrong = 0
    if n<0:
        print("Invalid! Please enter a positive number.")
    else:
        power = len(str(n))
        while num > 0:
            last_digit = num % 10
            armstrong += (last_digit**(power))
            num = num // 10
        if armstrong == n:
            print(f"Your number {n} is an Armstrong number.") 
        else:
            print(f"Your number {n} is not an Armstrong number.") 

except ValueError:
    print("Invalid! Please enter numeric digits.")
