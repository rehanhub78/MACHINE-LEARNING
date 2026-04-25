'''
Print pattern of characters (A, AB, ABC, ...) recursively.
'''
ch = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def char_pattern(n):
    if n > 0:
        char_pattern(n-1)
        for i in range(n):
            print(ch[i],end="")
        print()
# 2nd way to solve this:
def char_pattern2(n):
    if n > 0:
        char_pattern2(n-1)
        for i in range(n):
            print(chr(65+i),end="")
        print()
try:
    num = int(input("Enter number of rows: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num < 0:
    print("Invalid! Please enter a non-negative integer.")
else:
    char_pattern(num)
    char_pattern2(num)