'''
Count how many elements are even and odd.
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
even_count = 0
odd_count = 0
for i in my_array:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Number of even elements in your array is: {even_count}" )
print(f"Number of odd elements in your array is: {odd_count}" )