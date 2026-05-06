'''
 Print all unique elements (those that occur exactly once). 
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
double = []
for i in range(n):
    for j in range(i+1,n):
        if array[i] == array[j]:
            if array[i] not in double:
                double.append(array[i])

unique = [x for x in array if x not in double]
print("Unique elements (occurring exactly once):", unique)