'''
Take the hour of the day (0-23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”.
'''
a = int(input("Enter current hour: "))
if a in range(4,13):
    print("Good Morning")
elif a in range(13,17):
    print("Good Afternoon")
elif a in range(17,22):
    print("Good Evening")
else:
    print("Good Night")

