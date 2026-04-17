from datetime import date
a = int(input("Enter the year: "))
b = int(input("Enter today month: "))
c = int(input("Enter today date: "))
my_date= date(a ,b ,c)
print(my_date.strftime("%A"))
# using calender
import calendar
day = my_date.weekday()
print(calendar.day_name[day])