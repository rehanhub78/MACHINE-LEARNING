'''
Create a new array containing squares of all numbers.
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

squared_array = [i**2 for i in my_array]
print(f"Original array: {my_array}")
print(f"Array with squares of all numbers: {squared_array}")