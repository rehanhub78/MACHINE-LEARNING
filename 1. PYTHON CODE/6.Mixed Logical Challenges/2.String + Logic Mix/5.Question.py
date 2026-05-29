'''
Print characters that appear more than once (without map).
'''
s = input("Enter a string: ")
s = s.replace(" ", "").lower()
v =[]
for i in s:
    if s.count(i) > 1 and i not in v:
        v.append(i)
print(f"Characters that appear more than once: {v}")

