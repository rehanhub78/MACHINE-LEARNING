'''
Find the second smallest element in an array.
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
    print("There is no second smallest element in the array.")
else:
    smallest = float('inf')
    second_smallest = float('inf')
    for i in array:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i != smallest:
            second_smallest = i
    if second_smallest == float('inf'):
        print("There is no second smallest element in the array.")
    else:
        print(f"The second smallest element in the array is: {second_smallest}")