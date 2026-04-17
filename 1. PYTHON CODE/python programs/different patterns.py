a=input("enter type of pattern you want normal,opposite,reverse and center: ")
n = int(input("Enter the number of rows you want: "))
if a =="normal":
        for i in range(1,n+1):
            print("*"*(i))
elif a =="reverse":
    for i in range(0,n):
        print("*"*(n-i))
elif a =="opposite" :
     for i in range(1,n+1):
        print(" "*(n-i),"*"*(i))
elif a =="center" :
     for i in range(1,n+1):
        print(" "*(n-i),"*"*(2*i-1))
else :
     print("This pattern is not availaible")
