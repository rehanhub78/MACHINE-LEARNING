'''
 Print sum of first n terms of Fibonacci series. 
'''
try:
    n = int(input("Enter your number: "))

except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()

a = 0
b = 1
sum = 0
if n <= 0 :
    print("Invalid! Please enter a non-zero positive number.")
else:
    for i in range(n):
        total += a
        a , b =  b , a+b
    print(total)

print()
