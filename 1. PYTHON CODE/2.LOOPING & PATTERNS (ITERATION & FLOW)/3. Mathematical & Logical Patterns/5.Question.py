'''
Print all factors of a given number.
'''
try:
    num1 = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
if num1 == 0 :
    print("All numbers are factors of 0.")
else:
    n = abs(num1)
    a = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    print(f"Positive factors: {a}", end="\n")
    print(f"Negative factors: {[-x for x in a]}", end=" ")
print()