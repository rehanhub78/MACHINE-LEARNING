'''
 Print the sum of first n natural numbers.
'''
try:
    n = int(input("Enter a natural number: "))
    sum = 0
    if n <= 0:
        print("Enter a natural number: ")
    else:
        for i in range(1,n+1):
            sum += i
        print(sum)
except ValueError:
    print("Invalid! Please enter a numeric digit.")