'''
Print the second half of the string in reverse.
'''
n = input("Enter a string: ")
le = len(n)
s = list(n[le//2:])
l = 0
r = len(s) - 1
while l < r:
    s[l] , s[r] = s[r] , s[l]
    l += 1
    r -= 1
print(f"Second half in reverse is: {"".join(s)}")
