'''
Check if a given year is a leap year.
'''
a = int(input("Enter the year: "))
if a % 4 == 0:
    print("This year is a leap year.")
else:
    print("This year is not a leap year.")