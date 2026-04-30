'''
Check if all elements in an array are unique.
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
        
new_array = []
for i in my_array:
    if i not in new_array:
        new_array.append(i)
if my_array == new_array:
    print("Array is unique.")
else:
    print("Array is not unique.")    
