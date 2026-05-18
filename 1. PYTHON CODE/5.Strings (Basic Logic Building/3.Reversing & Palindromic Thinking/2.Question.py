'''
Reverse each word in a sentence.
'''
n = input("Enter a sentence: ")
words = n.split()
print("Reverse string is: ", end="")
for word in words:
    s = list(word)
    l = 0
    r = len(s) -1
    while l < r:
        s[l],s[r] = s[r],s[l]
        l += 1
        r -= 1
    s = "".join(s)
    print(f"{s} ", end="")