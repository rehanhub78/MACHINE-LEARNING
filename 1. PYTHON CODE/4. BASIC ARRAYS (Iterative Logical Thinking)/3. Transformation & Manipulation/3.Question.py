'''
Replace every negative number with 0. 
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
new_array = [i if i >= 0 else 0 for i in my_array]
print(f"Array after replacing negative number with 0 is: {new_array}")