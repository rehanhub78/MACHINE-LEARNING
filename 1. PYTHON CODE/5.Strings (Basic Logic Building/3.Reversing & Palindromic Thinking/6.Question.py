'''
Print the middle character(s) of a string.
'''
n = input("Enter a string: ")
l = len(n)
if l % 2 == 0:
    print(f"Middle characters are: {n[l//2-1:l//2+1]}")
else:
    print(f"Middle character is: {n[l//2]}")