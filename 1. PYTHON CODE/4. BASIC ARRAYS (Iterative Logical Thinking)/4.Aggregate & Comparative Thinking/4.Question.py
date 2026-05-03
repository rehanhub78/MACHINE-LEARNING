'''
Find the common elements between two arrays.
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
common_elements = []
if len(array1) != len(array2):
    print("arrays are not equal.")
else:
    for i in range(0,len(array1)):
        if array1[i] in array2 and array1[i] not in common_elements:
            common_elements.append(array1[i])
    if common_elements:
        print("Common elements:", common_elements)
    else:
        print("No common elements found.")
