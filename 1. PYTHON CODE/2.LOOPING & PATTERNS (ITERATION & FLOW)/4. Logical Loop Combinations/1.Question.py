'''
Print all numbers whose sum of digits is even (1-100). 
'''
for i in range(1,101):
    digits = [int(d) for d in str(i)]
    total = 0
    for j in digits:
        total += j
    if total % 2 ==0:
        print(i)
