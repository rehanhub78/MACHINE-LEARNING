'''
Print pattern of increasing characters (A, AB, ABC...). 
'''
for i in range(26):
    for j in range(i+1):
        print(chr(j+65), end="")
    print()


