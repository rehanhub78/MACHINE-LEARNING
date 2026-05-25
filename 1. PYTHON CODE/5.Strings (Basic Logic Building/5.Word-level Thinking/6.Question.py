'''
Print all words that start and end with the same letter.
'''
n = input("Enter a sentence: ")
s = n.split()
for i in s:
    if i[0] == i[len(i)-1]:
        print(i)
