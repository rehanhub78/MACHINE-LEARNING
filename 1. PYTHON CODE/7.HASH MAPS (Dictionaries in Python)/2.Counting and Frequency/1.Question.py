'''
count the frequency of each character in a given string.
'''
text = "rehan ali"
freq = {}
for char in text:
    freq[char] = freq.get(char,0)+1

print(freq)