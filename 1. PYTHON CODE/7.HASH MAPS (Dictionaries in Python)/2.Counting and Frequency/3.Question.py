'''
Find the first non-repeatimg character in a string and return its index.
'''
text = "hello my name is rehan"
freq = {}
for char in text:
    freq[char] = freq.get(char , 0) + 1

for i,char in enumerate(text):
    if freq[char] == 1:
        print(f"the first non-repeatimg character in a string is at index : {i}")
        break
