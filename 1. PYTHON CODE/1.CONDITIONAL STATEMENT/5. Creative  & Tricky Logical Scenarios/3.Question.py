'''
Take day and month and check if it forms a valid calendar date (ignoring leap years).
'''
while True:
    try:
        day = int(input("Enter day: "))
        month = int(input("Enter month: "))
        if day > 31 or day < 1:
            print("Enter correct day.")
            continue

        if month > 12 or month < 1:
            print("Enter correct month.")
            continue


        if (day <= 30 and month in [4,6,9,11]) or (day <= 28 and month == 2) or (day <= 31 and month in [1,3,5,7,8,10,12]):
            print("Valid calender date!.")
            break
        else:
            print("Invalid! that month does not have that many days.Please re-enter.")
    except ValueError:
        print("Invalid input! Please enter numeric digit.")

