'''
Find the maximum and minimum element in an array.
'''
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)
max_element = arr[0]
min_element = arr[0]
for element in arr:
    if element > max_element:
        max_element = element
    if element < min_element:
        min_element = element

print(f"Maximum element in the array: {max_element}")
print(f"Minimum element in the array: {min_element}")