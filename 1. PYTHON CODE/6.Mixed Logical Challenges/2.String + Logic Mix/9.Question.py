'''
Find the word with maximum vowels in a sentence.
'''
n = input("Enter a sentence: ")
words = n.split()
vowels = "aeiou"
max_vowels = 1
word = []
for i in words:
    count_vowels = 0
    for char in i:
        if char.lower() in vowels:
            count_vowels += 1
    if count_vowels > max_vowels:
        max_vowels = count_vowels
        word.clear()
        word.append(i)
    elif count_vowels == max_vowels:
        word.append(i)
print(word)
