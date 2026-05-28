'''
Check if a number is palindrome (121 → true).
'''
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()
original_num = n
reverse_num = 0
while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n //= 10
if original_num == reverse_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")