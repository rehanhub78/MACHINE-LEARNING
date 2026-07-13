'''
Print a multiplication table in a formatted grid (10x10).
'''
for i in range(1,11):
    for j in range(1,11):
        print(f"{i * j:4}", end=" ")
    print()
