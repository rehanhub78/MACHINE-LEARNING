'''
Replace every vowel in a string with its position (a=1, e=2...).
'''
def replace_vowels(s):
    vowels = 'aeiou'
    result = ''
    for char in s:
        if char.lower() in vowels:
            position = vowels.index(char.lower()) + 1
            result += str(position)
        else:
            result += char
    return result
input_string = input("Enter a string: ")
output_string = replace_vowels(input_string)
print(f"String after replacing vowels with their positions: {output_string}")