'''
Reverse an array (without using built-in reverse).
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
new_array = []
for i in range(len(my_array)-1,-1,-1):
    new_array.append(my_array[i])
print(f"Reverse array is: {new_array}")