'''
Count how many elements are perfect squares.
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
        
perfect_square_count = 0
for i in my_array:
    if i > 0:
        sqrt_i = int(i**0.5)
        if sqrt_i * sqrt_i == i:
            perfect_square_count += 1
# second method
ps_count = [i for i in my_array if i > 0 and int(i**0.5)**2 == i]
print(f"Count of perfect squares in the array: {perfect_square_count}")
print(f"Count of perfect squares in the array (second method): {len(ps_count)} \n{ps_count}")
