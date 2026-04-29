'''
Count how many times a given element appears.
'''
n = int(input("Enter how many numbers you want to store in the array: "))
if n <= 0:
    print("Invalid! Please enter a positive integer.")
    exit()
    
my_array = []
while len(my_array) < n:
    try:
        num = int(input(f"Enter number {len(my_array) + 1}: "))
        my_array.append(num)
    except ValueError:
        print("Invalid! Please enter numeric digit.")
try:
    b = int(input("Enter your number: "))
except ValueError:
        print("Invalid! Please enter numeric digit.")
num_count = 0
for i in my_array:
    if i == b:
        num_count += 1
print(f"Number {b} appears {num_count} times in array")