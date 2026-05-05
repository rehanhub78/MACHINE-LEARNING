'''
Check if the array is sorted in ascending order.
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
sorted_array = []
array1 = array.copy()
while len(array1) > 0:
    i = min(array1)
    sorted_array.append(i)
    array1.remove(i)
if array == sorted_array:
    print("The array is sorted in ascending order.")
else:
    print("The array is not sorted in ascending order.")
    