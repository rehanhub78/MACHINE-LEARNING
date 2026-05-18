'''
Print how many words start with a vowel in a sentence.
'''
def count_vowel_words(sentence):
    vowels = 'AEIOUaeiou'
    words = sentence.split()
    count = sum(1 for word in words if word[0] in vowels)
    return count
sentence = input("Enter a sentence: ")
print(f"Number of words that start with a vowel: {count_vowel_words(sentence)}")