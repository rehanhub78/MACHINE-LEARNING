'''
Take two numbers and check if both are positive and their sum is less than 100. 
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>=0 and b>=0:
    if (a+b)<100:
        print("both are positive and their sum is less than 100")
    else:
        print("both are positive but their sum is not less than 100")
else:
    print("both are not positive.")