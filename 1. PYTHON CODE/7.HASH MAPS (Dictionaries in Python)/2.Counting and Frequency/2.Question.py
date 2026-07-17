'''
fint the element in an array that appears more than n/2 times.
'''
arr = [2, 3, 3, 3, 4, 3, 3, 3, 5, 4, 5, 1, 4]
freq={}
for i in arr:
    freq[i] = freq.get(i,0) + 1
for key,value in freq.items():
    if value >= len(arr)//2:
        print(key ,end=" ")
print()