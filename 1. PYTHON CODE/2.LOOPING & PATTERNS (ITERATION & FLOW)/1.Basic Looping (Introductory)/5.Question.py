'''
 Print the sum of all even numbers up to n. 
'''
try:
    n = int(input("Enter a natural number: "))
    sum = 0
    if n <= 0:
        print("Enter a natural number: ")
    else:
        for i in range(2,n+1,2):
            sum += i
        print(sum)
except ValueError:
    print("Invalid! Please enter a numeric digit.")