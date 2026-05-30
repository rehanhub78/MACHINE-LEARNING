'''
Count words that start and end with the same letter.
'''
s = input("Enter a sentence: ")
words = s.split()
count = 0
for word in words:
    if word[0].lower() == word[-1].lower():
        count += 1
print(f"Number of words that start and end with the same letter: {count}")