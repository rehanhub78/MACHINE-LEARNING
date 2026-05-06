'''
Count how many elements are greater than the average of the array.
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
else:
    average = sum(array) / n
    count = 0
    for i in array:
        if i > average:
            count += 1
    print(f"The number of elements greater than the average is: {count}")
