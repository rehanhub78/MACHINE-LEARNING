'''
Print all palindromic words from a sentence.
'''
sentence = "Madam, I'm Adam. Was it a car or a cat I saw?"
words = sentence.split()
palindromes = []
for word in words:
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    if cleaned_word == cleaned_word[::-1] and len(cleaned_word) > 1:
        palindromes.append(word)
print(f"Palindromic words: {', '.join(palindromes)}")