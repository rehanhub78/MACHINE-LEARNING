'''
input an element x — check if it exists in the array. 
'''
my_array = [1,2,8,5,4,3,6,7,9,1,13,16,19,20,22,25,28,27,31,38,34,45,42,48,58,56,51,98,74,78,86,99]
try:
    num = int(input(f"Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
if num in my_array:
    print(f"Yes! {num} is blongs in array.")
else:
    print(f"No! {num} is not blongs in array.")