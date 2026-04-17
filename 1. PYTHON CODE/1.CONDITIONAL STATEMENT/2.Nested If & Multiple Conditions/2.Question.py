'''
If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.
'''

a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
if a + b > c and a + c > b and b + c > a:
    print("The sides form a valid triangle.")
    if a == b == c == a:
        print("This triangle is equilateral")
    elif a == b or b == c or c == a :
        print("this triangle is isosceles")
    else:
        print("This triangle is scalene")
else:
    print("The sides do not form a valid triangle.")



