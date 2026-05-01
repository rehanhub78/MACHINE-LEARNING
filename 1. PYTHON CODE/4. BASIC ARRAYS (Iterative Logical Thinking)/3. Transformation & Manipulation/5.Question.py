'''
Swap the first and last elements of the array.
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
if len(my_array) > 1:
    my_array[0], my_array[-1] = my_array[-1], my_array[0]
print(f"Array with first and last elements swapped: {my_array}")