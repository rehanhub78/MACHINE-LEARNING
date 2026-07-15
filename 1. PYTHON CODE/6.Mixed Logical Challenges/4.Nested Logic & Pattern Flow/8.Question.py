'''
Print Pascal’s triangle up to N rows.
'''
N = int(input("Enter the number of rows for Pascal's triangle: "))
for i in range(N):
    print(' ' * (N - i - 1), end='')
    value = 1
    for j in range(i + 1):
        print(value, end=' ')
        value = value * (i - j) // (j + 1)
    print()