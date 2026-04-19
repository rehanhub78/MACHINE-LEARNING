'''
Print all numbers between a and b divisible by 7. 
'''
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number:  "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()

start_num , end_num = sorted([a,b])
for i in range(start_num,end_num+1):
    if i % 7 == 0:
        print(i ,end=" ")

print()