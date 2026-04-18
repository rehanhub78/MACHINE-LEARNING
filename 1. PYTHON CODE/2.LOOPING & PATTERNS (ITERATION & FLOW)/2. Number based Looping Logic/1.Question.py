'''
Count the number of digits in a given number.
'''
try:
    n = int(input("Enter a number: "))
    n = abs(n)
#     digit = [int(d) for d in str(n)]
#     print("Number of digits in your number is:",len(digit))
    count = 0
    if n == 0:
        count = 1
    else:
        while n>0:
            n = n // 10
            count += 1
    print(f"Number of digits in your number is {count}") 
except ValueError:
    print("Invalid! enter numeric digit.")
