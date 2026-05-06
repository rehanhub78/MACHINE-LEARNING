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
    sorted_array = []
    array1 = array.copy()
    while len(array1) > 0:
        i = min(array1)
        sorted_array.append(i)
        array1.remove(i)
    sum_of_elements = sum(sorted_array[1:-1])
    print(f"The sum of all elements except the largest and smallest is: {sum_of_elements}")