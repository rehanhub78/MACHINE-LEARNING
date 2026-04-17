'''
Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.
'''
a = int(input("Enter the tempreature in celsius 0 to 100: "))
if a in range(0,26):
    print("COLD")
elif a in range(26,51):
    print("WARM")
else :
    print("HOT")
