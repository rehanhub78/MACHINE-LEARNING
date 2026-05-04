'''
Create a frequency array of numbers (count occurrence of each number).
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
print("Frequency of each number:")
for num, count in frequency.items():
    print(f"{num}: {count}")
