'''
Take time (hours and minutes) and print the smaller angle between the hour and minute hands
'''
while True:
    try:
        print("Enter time:")
        hour = float(input("hour: "))
        minute = float(input("minute: "))
        if hour<=0 or hour>12:
            print("Invalid! Please enter correct hour.")
            continue
        if minute<0 or minute>=60:
            print("Invalid! Please enter correct minute(0-59).")
            continue

        angle = abs(30*hour - 5.5*minute)
        if angle<=180:
            print(f"The smaller angle between the hour and minute hands {angle}")
            break
        else:
            print(f"The smaller angle between the hour and minute hands {360 - angle}")
            break

    except ValueError:
        print("Invalid input! Please enter numeric digit.")

