'''
Find the sum of all elements in an array.
'''
n = int(input("Enter how many numbers you want to store in the array: "))
my_array = []
while len(my_array) < n:
    try:
        num = int(input(f"Enter number {len(my_array) + 1}: "))
        my_array.append(num)
    except ValueError:
        print("Invalid! Please enter numeric digit.")
sum_array = 0
for i in my_array:
    sum_array += i

print(f"Sum of your array is: {sum_array}")