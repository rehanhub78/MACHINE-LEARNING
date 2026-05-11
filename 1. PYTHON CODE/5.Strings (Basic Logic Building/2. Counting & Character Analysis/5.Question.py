'''
Count how many spaces are there in a sentence. 
'''
def count_spaces(sentence):
    count = 0
    for char in sentence:
        if char == ' ':
            count += 1
    return count
sentence = input("Enter a sentence: ")
spaces = count_spaces(sentence)
print(f"The number of spaces in the sentence is: {spaces}")