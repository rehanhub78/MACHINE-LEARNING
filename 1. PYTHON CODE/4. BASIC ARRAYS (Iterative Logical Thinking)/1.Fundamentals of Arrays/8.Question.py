'''
Find the index of the maximum element.
'''
n = int(input("Enter how many numbers you want to store in the array: "))
if n <= 0:
    print("Invalid! Please enter a positive integer.")
    exit()
    
my_array = []
while len(my_array) < n:
    try:
        num = int(input(f"Enter number {len(my_array) + 1}: "))
        my_array.append(num)
    except ValueError:
        print("Invalid! Please enter numeric digit.")
max_index = my_array[0]
for i in my_array:
    if i > max_index:
        max_index = i
print(f"The maximum element index in your array is: {my_array.index(max_index)}")
