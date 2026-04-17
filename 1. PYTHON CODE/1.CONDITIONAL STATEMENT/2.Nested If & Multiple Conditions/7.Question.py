'''
 Take a month number (1–12) and print the number of days in that month (ignore leap years).
'''
a = int(input("Enter month number: "))
b = [1,3,5,7,8,10,12]
c = [4,6,9,11]
if a in b:
    print(31,"days")
elif a in c:
    print(30,"days")
elif a==2:
    print(28,"days")
else:
    print("This month does not exist.")