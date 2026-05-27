'''
Find the sum of digits of a number (use loop).
'''
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Enter a valid integer.")
    exit()
sum = 0
for i in str(abs(n)):
    sum += int(i)
print(f"Sum of digits of {n} is: {sum}")