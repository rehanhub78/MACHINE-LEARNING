'''
Count how many words contain the letter 'a'.
'''
n = input("Enter a sentence: ")
s = n.split()
count = 0
for i in s:
    if "a" in i:
        count += 1
print(f"Total words contains the letter 'a' is: {count}")
