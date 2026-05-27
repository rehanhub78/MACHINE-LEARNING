'''
Check if a number is an Armstrong number.
'''
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Enter a valid integer.")
    exit()
sum = 0
n = abs(n)
power = len(str(n))
for i in str(n):
    sum += int(i)**power
if n == sum:
    print("Your number is an armstrong number.")
else:
    print("Your number is not an armstrong number.")