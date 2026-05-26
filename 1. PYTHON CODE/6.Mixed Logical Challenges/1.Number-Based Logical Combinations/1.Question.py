'''
Print all numbers between 1 and N that are divisible by both 3 and 5.
'''
try:
    n = int(input("Enter number: "))
except ValueError:
    print("Enter a integer value.")
    exit()
for i in range(15, n+1, 15):
    print(i , end = " ")
