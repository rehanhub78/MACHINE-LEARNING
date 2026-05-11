'''
Find the frequency of each character in a string (without using a map).
'''
def count_characters(s,char=None):
    if char is None:
        char = []
    if s[0] not in char:
        frequency = 0
        for c in s:
            if c == s[0]:
                frequency += 1
        print(f"The frequency of '{s[0]}' is: {frequency}")
        char.append(s[0])
    return count_characters(s[1:], char) if len(s) > 1 else None

n = input("Enter a string: ")
count_characters(n)
        
