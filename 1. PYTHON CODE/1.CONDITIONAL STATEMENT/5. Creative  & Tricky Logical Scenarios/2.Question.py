'''
Take three numbers and check if they can form a Pythagorean triplet.
'''
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
# if a*a == c*c + b*b or b*b == a*a +c*c or c*c == a*a + b*b:
#     print(a,b,c,"form a Pythagorean triplet.")
# else:
#     print(a,b,c,"do not form Pythagorean triplet.")

import math
sides =sorted([a,b,c])
hypotenuse_squred = sides[2]**2
legs_squared = sides[0]**2 + sides[1]**2
if math.isclose(hypotenuse_squred,legs_squared):
    print(a,b,c,"form a Pythagorean triplet.")
else:
    print(a,b,c,"do not form a Pythagorean triplet.")

