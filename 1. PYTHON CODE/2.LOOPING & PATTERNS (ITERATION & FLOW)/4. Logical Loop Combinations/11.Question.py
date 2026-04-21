'''
Take 5 numbers as input. If the user enters 0, skip it using continue. At the end, print the sum of all non-zero numbers entered.
'''
total = 0
for i in range(1,6):
    try:
        num = int(input(f"Enter number {i}: "))
    except ValueError:
        print("Invalid! Please enter numeric digits.")
        exit()
    if num == 0:
        continue

    total += num
print(f"The sum of all non-zero numbers entered is: {total}")
