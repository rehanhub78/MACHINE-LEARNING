'''
Count how many positive, negative, and zero elements are in an array.
'''
try:
    n = int(input("Enter the number of elements in the array: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

arr = []
for i in range(n):
    while True:
        try:
            element = int(input(f"Enter element {i + 1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    arr.append(element)

    positive_count = 0
    negative_count = 0
    zero_count = 0

for element in arr:
    if element > 0:
        positive_count += 1
    elif element < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Number of positive elements: {positive_count}")
print(f"Number of negative elements: {negative_count}")
print(f"Number of zero elements: {zero_count}")