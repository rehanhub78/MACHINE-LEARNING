'''
Count how many words end with 's'.
'''
def count_word(s):
    words = s.split()
    words = sum(1 for words in words if words[-1] == "s")
    return words
n = input("Enter a sentence: ")
print(f"Number of words that end with 's' is: {count_word(n)}")
