'''
Find element-wise product of two arrays.
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
if len(array1) == 0 or len(array2) == 0:
    print("One or both arrays are empty.")
else:
    for i in range(min(len(array1), len(array2))):
        product_array = array1[i] * array2[i]
        print(f"Product of element {i+1} of both arrays is: {product_array}")
