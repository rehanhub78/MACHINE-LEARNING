'''
Count how many words have even length.
'''
n = input("Enter a sentence: ")
s = n.split()
count = 0
for i in s:
    if len(i) % 2 == 0:
        count += 1
print("Number of words with even length:", count)