'''
Take a weekday number (1-7) and determine if it is a weekday or weekend.
'''
while True:
    try:
        day = int(input("Enter weekday number(1-7) 1 for monday and 7 for sunday: "))
        hour = int(input("Enter hour (0-23): "))
        if day>7 or day<1:
            print("Enter correct weekday.")
            continue

        if hour > 23 or hour < 0:
            print("Enter correct hour.")
            continue

        if day in range(1,6):
            if hour in range(9,18):
                print("At Work")
            else:
                print("Resting")
        else:
            print("Party Time")
        break
    except ValueError:
        print("Invalid input! Please enter weekday and hour in numeric digit.")
