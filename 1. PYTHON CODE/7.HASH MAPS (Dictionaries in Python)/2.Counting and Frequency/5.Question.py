'''
count the occurences of each word in a given sentences, ignoring punctution and capitilization.
'''
sent = "this is question of practice of hashmap in python"
freq = {}
for char in sent.replace(" ","").lower():
    freq[char] = freq.get(char,0) +1
for key,value in freq.items():
    print(f"{key}:{value}", end=",")

print()