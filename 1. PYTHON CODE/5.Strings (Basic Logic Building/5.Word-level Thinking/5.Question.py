'''
Swap first and last words in a sentence.
'''
n = input("Enter a sentence: ")
s = n.split()
s[0],s[len(s)-1] = s[len(s)-1],s[0]
print(f"Sentence after swaping first and last word is: {" ".join(s)}")
