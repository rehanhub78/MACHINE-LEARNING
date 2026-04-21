'''
Find the smallest and largest digit in a given number. 
'''
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()

digits = [int(d) for d in str(abs(num))]
smallest = digits[0]
largest = digits[0]
for i in digits:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i

print(f"Largest digit is: {largest}")
print(f"Smallest digit is: {smallest}")
