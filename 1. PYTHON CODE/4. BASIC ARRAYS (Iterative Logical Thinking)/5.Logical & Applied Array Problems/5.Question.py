'''
Find the difference between the largest and smallest element.
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
    print(f"The difference between the largest and smallest element in the array is: {max(array) - min(array)}")
