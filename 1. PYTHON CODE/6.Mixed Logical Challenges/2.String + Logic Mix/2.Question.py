'''
Count vowels in each word of a sentence.
'''
def count_vowels(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    vowel_counts = {}
    for word in words:
        count = sum(1 for char in word if char.lower() in vowels)
        vowel_counts[word] = count
    return vowel_counts
sentence = input("Enter a sentence: ")
vowel_counts = count_vowels(sentence)
print("Vowel counts for each word:", vowel_counts)