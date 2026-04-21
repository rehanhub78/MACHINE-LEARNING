'''
 Print all numbers from 1-n whose binary representation has an even number of 1s. 
'''
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
n= abs(num)
for i in range(1,n+1):
    temp = i
    ones_count = 0
    while temp > 0:
        remainder = temp % 2
        if remainder == 1:
            ones_count += 1
        temp //= 2
    if ones_count % 2 == 0:
        print(i , end=" ")
print()
            