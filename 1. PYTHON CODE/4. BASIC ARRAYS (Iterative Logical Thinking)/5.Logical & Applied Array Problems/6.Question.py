'''
Find the sum of all elements except the largest and smallest.
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
    print("There is only one element in the array.")
elif n == 2:
    print("There are only two elements in the array.")
else:
    largest = float('-inf')
    smallest = float('inf')
    for i in array:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    filter = [x for x in array if x != largest and x!= smallest]
    result = sum(filter)
    print(f"The sum of all elements except the largest and smallest is: {result}")
