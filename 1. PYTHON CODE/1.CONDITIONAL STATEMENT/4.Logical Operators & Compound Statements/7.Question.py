'''
Take electricity units consumed and calculate the bill as per slabs (using if-else).
'''
unit = int(input("Enter your consumed Electricity units: "))
if unit <= 100:
    bill = unit * 5
elif unit <= 200:
    bill = 100 * 5 + (unit - 100) * 10
else:
    bill = 100 * 5 + 100 * 10 + (unit - 200) * 15
print("Your electricity bill is: Rs.", bill)