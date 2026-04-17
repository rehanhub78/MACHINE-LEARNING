'''
Take two angles of a triangle and compute the third angle.
'''
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
if a>0 and b>0 and (a+b) < 180:
    print("Third angle is =",180-a-b)
else:
    print("This triangle is not possible.")