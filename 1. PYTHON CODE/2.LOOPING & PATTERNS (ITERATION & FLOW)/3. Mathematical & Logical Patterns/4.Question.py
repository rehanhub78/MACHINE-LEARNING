'''
Find LCM of two numbers using loops. 
'''
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
a = abs(num1)
b = abs(num2)
start_num, end_num = sorted([a,b])
lcm = 0
if a == 0 or b == 0:
    print("LCM of 0 is undefined.")
else:
    for i in range(end_num,((a*b)+1),end_num):
        if i % a == 0 and i % b == 0:
            lcm += i
            break 
    print(f"The LCM of {num1} and {num2} is: {lcm}")