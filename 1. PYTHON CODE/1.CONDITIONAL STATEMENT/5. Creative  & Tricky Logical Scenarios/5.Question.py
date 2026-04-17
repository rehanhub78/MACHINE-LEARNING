'''
Take three numbers and check if they are in arithmetic progression.
'''
import math
while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
        ap_list = sorted([a,b,c])
        diff1 = ap_list[1]-ap_list[0]
        diff2 = ap_list[2]-ap_list[1]
        if math.isclose(diff1,diff2):
            print(f"{ap_list} are in arithmetic progression.")
            break
        else:
            print(f"{ap_list} are not in arithmetic progression.")

    except ValueError:
        print("Invalid input! Please enter numeric digit.")

        