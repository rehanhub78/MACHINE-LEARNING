'''
Take two dates (day and month) and determine which one comes first in the calendar. 
'''
while True:
    try:
        print("Enter Date 1:")
        day1 = int(input("day1: "))
        month1 = int(input("month1: "))
        date1 = [day1,month1]

        print("Enter Date2")
        day2 = int(input("day2: "))
        month2 = int(input("month2: "))
        date2 = [day2,month2]

        if day1 <= 0 or day2 <=0 or day1 > 31 or day2 >31:
             print("enter correct date.")
             continue

        if month1<1 or month2<1 or month1>12 or month2>12:
            print("Enter correct month.")
            continue

        if month1 == month2:
            if day1 == day2:
                print("Both are same date.")
                break
            elif day1<day2:
                print(f"Date 1 {date1} comes first.")
                break
            else:
                print(f"Date 2 {date2} comes first.")
                break
        elif month1 < month2:
            print(f"Date 1 {date1} comes first.")
            break
        else:
            print(f"Date 2 {date2} comes first.")
            break
    except ValueError:
        print("Invalid input! Please enter numeric digit.")

        