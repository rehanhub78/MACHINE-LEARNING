'''
Reverse a string without using built-in reverse.
'''
n = input("Enter a string: ")
s = list(n)
l = 0
r = len(s) -1
while l < r:
    s[l],s[r] = s[r],s[l]
    l += 1
    r -= 1
s = "".join(s)
print(f"Reverse string is: {s}")