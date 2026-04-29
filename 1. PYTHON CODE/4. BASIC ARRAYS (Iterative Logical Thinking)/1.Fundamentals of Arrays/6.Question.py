'''
Count how many elements are positive, negative, or zero.
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
positive_count = 0
negative_count = 0
zero_count = 0
for i in my_array:
    if i>0:
        positive_count += 1
    elif i<0:  
        negative_count += 1
    else:
        zero_count += 1

print(f"Number of positive elements in your array is: {positive_count}")
print(f"Number of negative elements in your array is: {negative_count}")
print(f"Number of zero elements in your array is: {zero_count}")
