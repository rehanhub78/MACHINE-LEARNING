'''
Find the longest word in a sentence.
'''
n = input("Enter a sentence: ")
s = n.split()
longest = s[0]
for i in s:
    if len(i) > len(longest):
        longest = i
print(f"Longest word: {longest}")