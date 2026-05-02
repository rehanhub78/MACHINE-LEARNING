'''
Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.).
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


for i in range(0,len(my_array)-1,2):
    my_array[i],my_array[i+1] = my_array[i+1],my_array[i]
print(f"Swap array is: {my_array}")