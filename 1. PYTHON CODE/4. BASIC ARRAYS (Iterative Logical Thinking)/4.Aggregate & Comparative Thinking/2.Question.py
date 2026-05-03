'''
Compare two arrays — check if they contain the same elements (ignore order).
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
        
if len(array1) != len(array2):
    print("arrays are not equal.")
else:
    isequal = True
    for i in range(0,len(array1)):
        if array1[i] not in array2:
            print(f"Element {array1[i]} from array1 is not in array2.")
            isequal = False
            break
    if isequal:
        print("Array2 contains all elements of array1.")