'''
Remove duplicate words from a sentence.
'''
n = input("Enter a sentence: ")
words = n.split()
if len(words) == 0:
    print("No words in the sentence.")
else:
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    print(" ".join(unique_words))
