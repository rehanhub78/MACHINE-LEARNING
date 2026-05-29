'''
Reverse words in a string if their length is even.
'''
n = input("Enter a string: ")
def reverse_even_words(s):
    words = s.split()
    for i in range(len(words)):
        if len(words[i]) % 2 == 0:
            words[i] = words[i][::-1]
    return ' '.join(words)
result = reverse_even_words(n)
print(f"String after reversing even length words: {result}")