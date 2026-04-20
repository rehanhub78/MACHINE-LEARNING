'''
Check if a number is a strong number (sum of factorials of digits = number).
'''
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()

if num < 0 :
    print("Invalid! Please enter a positive number.")
else:
    digits = [int(d) for d in str(num)]
    total = 0
    fact = 1
    for i in digits:
        for j in range(1,i+1):
            fact *=j
        total, fact = total + fact , 1
    if total == num:
        print(f"Your number {num} is a strong number.")
    else:
        print(f"Your number {num} is not a strong number.")

    
