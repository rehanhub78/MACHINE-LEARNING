'''
Check if one of two given numbers is a multiple of the other.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a%b==0:
    print(a,"is the multiple of",b)
elif b%a==0:
    print(b,"is the multiple of",a)
else:
    print("they are not a multiple of each othe.")