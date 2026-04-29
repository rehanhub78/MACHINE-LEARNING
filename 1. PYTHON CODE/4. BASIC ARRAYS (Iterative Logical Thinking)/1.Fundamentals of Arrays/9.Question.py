'''
Take n elements and print only those greater than a given value k. 
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
k = int(input("Enter the value of k: "))
"give me 'i' , for every 'i' in 'my_array', if 'i' is greater than 'k'"
greater_element = [i for i in my_array if i > k] 
if not greater_element:
    print(f"No element greater than {k} in your array.")
else:
    print(f"The element greater than {k} in your array is: {greater_element}")
