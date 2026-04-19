'''
Print all factors of a given number.
'''
try:
    num1 = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
if num1< 0 :
    for i in range(num1,abs(num1)+1):
        if i == 0:
            continue
        elif num1 % i == 0:
            print(i, end=" ")
        
elif num1 >= 0 :
    for i in range(1,num1+1):
        if num1 % i == 0:
            print(i, end=" ")
print()