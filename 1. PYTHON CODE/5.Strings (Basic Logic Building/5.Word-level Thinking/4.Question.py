'''
Find the shortest word in a sentence.
'''
n = input("Enter a sentence: ")
s = n.split()
shortest = s[0]
for i in s:
    if len(i) < len(shortest):
        shortest = i
print(f"Shortest word: {shortest}")