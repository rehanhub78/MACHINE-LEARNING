'''
Toggle case for every alternate word in a sentence.
'''
def toggle_case(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].swapcase()
    return ' '.join(words)
# Example usage
input = "Hello World This is a Test"
output = toggle_case(input)
print(output)