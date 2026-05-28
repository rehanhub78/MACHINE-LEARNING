'''
Print the reverse of a number (123 → 321).
'''
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()
reverse_num = 0
while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n //= 10
print("Reverse of the number:", reverse_num)