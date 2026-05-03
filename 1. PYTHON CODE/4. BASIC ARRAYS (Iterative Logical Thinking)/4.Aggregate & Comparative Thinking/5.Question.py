'''
Find elements that are in one array but not in the other.
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
if len(array1) == 0 or len(array2) == 0:
    print("One or both arrays are empty.")
else:
    for i in array1:
        if i not in array2 and i not in common_elements:
            common_elements.append(i)
    for i in array2:
        if i not in array1 and i not in common_elements:
            common_elements.append(i)
if common_elements:
    print("Elements in one array but not in the other is:", common_elements)
else:
    print("No unique elements found in either array.")
