'''
Find the second largest element in an array.
'''
n = int(input("Enter how many numbers you want to store in the array: "))
if n <= 0:
    print("Invalid! Please enter a positive integer.")
    exit()  
array = []
while len(array) < n:
    try:
        num = int(input(f"Enter number {len(array) + 1}: "))
        array.append(num)
    except ValueError:
        print("Invalid! Please enter numeric digit.")
if n == 1:
    print("There is no second largest element in the array.")
else:
    sorted_array = []
    array1 = array.copy()
    while len(array1) > 0:
        i = max(array1)
        sorted_array.append(i)
        array1.remove(i)
    print(f"The second largest element in the array is: {sorted_array[1]}")