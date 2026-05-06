'''
Count how many pairs of elements have a sum equal to a given number k.
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
    k = 5 # You can change this value to test with different sums
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == k:
                count += 1
    print(f"The number of pairs with sum equal to {k} is: {count}")