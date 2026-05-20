'''
Check if two strings are the reverse of each other.
'''
n1 = input("Enter first string: ")
n2 = input("Enter second string: ")
s = list(n1)
l = 0
r = len(s) - 1
while l < r:
    s[l] , s[r] = s[r] , s[l]
    l += 1
    r -= 1
s = "".join(s)
print(f"Is strings are the reverse of each other: {s==n2}")