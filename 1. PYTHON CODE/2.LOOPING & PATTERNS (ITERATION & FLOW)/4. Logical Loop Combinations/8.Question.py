'''
Print a pattern where each row i prints i*i. 
'''
row = int(input("Enter number of Rows: "))
for i in range(1,row+1):
    for j in range(i):
        print(i, end="")
    print()
    