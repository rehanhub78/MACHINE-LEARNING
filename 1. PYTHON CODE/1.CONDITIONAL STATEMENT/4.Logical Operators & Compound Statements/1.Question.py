'''
Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and “FizzBuzz” if divisible by both.
'''
while True:
    a = int(input("Enter a number: "))
    if a%3==0 and a%5==0:
        print("“FizzBuzz”")
        break
    elif a%3==0:
        print("“Fizz”")
        break
    elif a%5==0:
        print("“Buzz”")
        break
    else:
        print("Enter another number.")
    