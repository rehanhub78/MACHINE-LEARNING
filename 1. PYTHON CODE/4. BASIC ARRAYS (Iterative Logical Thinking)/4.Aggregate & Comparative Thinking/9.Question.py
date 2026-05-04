'''
Print all elements that appear more than once.
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
frequency = {}
for num in array:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
exist = any(count > 1 for count in frequency.values())
if exist:
    print("Elements that appear more than once:")
    for num, count in frequency.items():
        if count > 1:
            print(f"{num}")
else:
    print("there are no elements that appear more than once.")
