'''
Find the first occurrence of a given number.
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
        exit()
if b not in my_array:
    print(f"Number {b} does not exist in array.")
else:
    print(f"Number {b} first occurs on index {my_array.index(b)}")
    