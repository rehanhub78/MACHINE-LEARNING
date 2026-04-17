'''
Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin. 
'''
print("Enter coordinates: ")
X = float(input("x: "))
Y = float(input("y: "))
if X == 0 and Y == 0:
    print("Origin")
elif X != 0 and Y == 0:
    print("X-Axis")
elif X == 0 and Y != 0:
    print("Y-Axis")
else:
    print("Your point lies in Quadrant.")

