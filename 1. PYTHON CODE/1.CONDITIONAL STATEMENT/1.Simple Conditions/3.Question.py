'''
Check if a number is divisible by both 3 and 5.
'''

a = int(input("Enter a number: "))
if a % 3 == 0 and a%5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")