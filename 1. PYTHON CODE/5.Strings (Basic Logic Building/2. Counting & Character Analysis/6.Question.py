'''
Count how many times a given character appears in a string.
'''
def count_character(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count
string = input("Enter a string: ")
character = input("Enter a character to count: ")  
occurrences = count_character(string, character)