def calculator():
    c = input("enter the expression or stop : ")
    a = int(input("enter no a: "))
    b = int(input("enter no b: "))
    if c == "+":
        print(a+b)
        return calculator()
    elif c == "-":
        print(a-b)
        return calculator()
    elif c == "*":
        print(a*b)
        return calculator()
    elif c == "/":
        print(a/b)
        return calculator()
    elif c == "%":
        print(a%b)
        return calculator()
    elif c == "^":
        print(pow(a,b))
        return calculator()
    elif c == "sqrt":
        print(pow(a,1/b))
        return calculator()
    elif c == "stop":
        print("Thanks for using")
    else :
        print("This expression is not available")
        return calculator()
calculator()
