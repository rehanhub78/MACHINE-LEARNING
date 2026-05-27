'''
Print all Armstrong numbers between 1 and 1000.
'''
j = 1
while j <= 10000:
    sum = 0
    power = len(str(j))
    for i in str(j):
        sum += int(i)**power
    if j == sum:
        print(j , end = " ")
    j += 1
