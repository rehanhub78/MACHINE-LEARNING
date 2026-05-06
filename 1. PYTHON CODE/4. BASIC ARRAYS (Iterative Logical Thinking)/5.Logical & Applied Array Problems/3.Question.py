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
    largest = float('-inf')
    second_largest = float('-inf')
    for i in array:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    if second_largest == float('-inf'):
        print("There is no second largest element in the array.")
    else:
        print(f"The second largest element in the array is: {second_largest}")