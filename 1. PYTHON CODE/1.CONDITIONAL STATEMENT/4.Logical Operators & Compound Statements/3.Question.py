'''
Take 24-hour time (hours and minutes) and print whether it is AM or PM.
'''
a = int(input("Enter hour: "))
b = int(input("Enter minutes: "))
if a in range(0,24) and b in range(0,60):
    if a<12:
        print(a,":",b,"AM")
    else:
        print(a,":",b,"PM")
else:
    print("Enter valid time.")