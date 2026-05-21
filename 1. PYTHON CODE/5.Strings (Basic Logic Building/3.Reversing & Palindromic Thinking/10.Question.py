'''
Reverse string but skip spaces.
'''
n = input("Enter a string: ")
l = 0 
r = len(n) -1
s = list(n)
while l<r:
    if s[l].isspace():
        l += 1
    elif s[r].isspace():
        r -= 1
    else:
        s[l],s[r] = s[r],s[l]
        l += 1
        r -= 1
print(f"reverse string is: {"".join(s)}")
