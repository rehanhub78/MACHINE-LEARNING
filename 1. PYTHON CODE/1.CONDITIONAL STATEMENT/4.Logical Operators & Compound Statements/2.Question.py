'''
Take three numbers and print the median value (neither maximum nor minimum). 
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
s = [a,b,c]
s.sort()
print("The median value of",a,",",b,",",c,",","is =",s[1])