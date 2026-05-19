'''
Reverse the order of words in a sentence.
'''
n = input("Enter a sentence: ")
words = n.split()
print("Reverse string is: ", end="")
l = 0
r = len(words) -1
while l < r:
    words[l],words[r] = words[r],words[l]
    l += 1
    r -= 1
print(" ".join(words))
