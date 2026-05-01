'''
Replace all even numbers with 1 and all odd with 0.
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
new_array = [1 if i % 2 == 0 else 0 for i in my_array]
print(f"Array after replacing even numbers with 1 and odd numbers with 0 is: {new_array}")