'''
Check if a number is a palindrome. 
'''
try:
    n = int(input("Enter your number: "))
    num = n
    reverse_num = 0
    while num > 0 :
        last_digit = num % 10
        reverse_num = (reverse_num*10) + last_digit
        num = num //10

    if n == reverse_num:
        print(f"Your number {n} is a palindrome")
    else:
        print(f"Your number {n} is not a palindrome")
except ValueError:
    print("Invalid! Please enter numeric digit.")
