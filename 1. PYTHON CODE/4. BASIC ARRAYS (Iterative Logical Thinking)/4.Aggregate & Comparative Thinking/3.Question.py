'''
Merge two arrays into a third array.
'''
n = int(input("Enter how many numbers you want to store in the array1: "))
if n <= 0:
    print("Invalid! Please enter a positive integer.")
    exit()
    
array1 = []
while len(array1) < n:
    try:
        num = int(input(f"Enter number {len(array1) + 1}: "))
        array1.append(num)
    except ValueError:
        print("Invalid! Please enter numeric digit.")
m = int(input("Enter how many numbers you want to store in the array2: "))

if m <= 0:
    print("Invalid! Please enter a positive integer.")
    exit()

array2 = []
while len(array2) < m:
    try:
        num = int(input(f"Enter number {len(array2) + 1}: "))
        array2.append(num)
    except ValueError:
        print("Invalid! Please enter numeric digit.")
merged_array = array1 + array2
print("Merged Array:", merged_array)
