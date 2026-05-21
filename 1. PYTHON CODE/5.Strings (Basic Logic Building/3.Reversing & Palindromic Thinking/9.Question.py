'''
Reverse only characters, keeping digits in place.
'''
n = input("Enter a string: ")
l = 0 
r = len(n) -1
s = list(n)
while l<r:
    if s[l].isdigit():
        l += 1
    elif s[r].isdigit():
        r -= 1
    else:
        s[l],s[r] = s[r],s[l]
        l += 1
        r -= 1
print(f"reverse string is: {"".join(s)}")
