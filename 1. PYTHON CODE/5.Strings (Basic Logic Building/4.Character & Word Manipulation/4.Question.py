'''
Replace all spaces with '_'.
'''
n = input("Enter a string: ")
s = list(n)
for i in range(len(s)):
    if s[i].isspace():
        s[i] = "_"
print(f"New string is: {"".join(s)}")