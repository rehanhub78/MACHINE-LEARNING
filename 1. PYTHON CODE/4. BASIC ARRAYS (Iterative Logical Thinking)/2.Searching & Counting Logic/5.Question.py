'''
Find the sum of even and odd elements only.
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
        
sum_even = 0
sum_odd = 0
for i in my_array:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"Sum of even elements: {sum_even}")
print(f"Sum of odd elements: {sum_odd}")
   