'''
Check if a number is a palindrome using recursion.
'''
def get_reverse(n , reversed_n=0):
    if n == 0:
        return reversed_n
    else:
        last_digit = n % 10
        new_reversed = (reversed_n*10) + last_digit
        return get_reverse(n // 10,new_reversed)

try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
b = get_reverse(abs(num))
if abs(num) == b:
    print("Palindrome",)
else:
    print("Not Palindrome")
