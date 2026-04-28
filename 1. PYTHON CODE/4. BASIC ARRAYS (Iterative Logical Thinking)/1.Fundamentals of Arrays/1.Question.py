'''
Input n and take n integers into an array; print them. 
'''
n = int(input("Enter how many numbers you want to store in the array: "))
my_array = []
for i in range(1,n+1):
    num = int(input(f"Enter number {i}: "))
    my_array.append(num)
print(f"Your array is: {my_array}")
