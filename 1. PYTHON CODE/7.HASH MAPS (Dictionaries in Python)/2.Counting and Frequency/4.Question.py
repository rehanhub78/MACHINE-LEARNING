'''
Check if two strings are anangrams of each other by comparing thei character frequency counyts.
'''
text1 = "abcdefghabcd"
text2 = "aabbccddefgh"
freq1 = {}
freq2 = {}

for char in text1.replace(" ","").lower():
    freq1[char] = freq1.get(char , 0) + 1
for char in text2.replace(" ","").lower():
    freq2[char] = freq2.get(char , 0) + 1

if freq1 == freq2:
    print("The strings are anangrams of each other")
else:
    print("The strings are not anangrams of each other")