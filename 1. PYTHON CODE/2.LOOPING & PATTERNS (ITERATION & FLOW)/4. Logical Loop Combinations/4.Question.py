'''
Print numbers between 1-100 whose digits add up to a multiple of 3. 
'''
for i in range(1,101):
    digits = [int(d) for d in str(i)]
    total = 0
    for j in digits:
        total += j
    if total % 3 == 0:
        print(i, end=" ")

print()