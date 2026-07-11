'''
Print all unique elements from an array.
'''
arr = [1,2,3,3,4,3,4,4,5,5,6,7,8,9,8,8,9,]
right= []
wrong = []
for i in arr:
    if i in right:
        right.remove(i)
        wrong.append(i)
    elif i not in wrong:
        right.append(i)
print(right)