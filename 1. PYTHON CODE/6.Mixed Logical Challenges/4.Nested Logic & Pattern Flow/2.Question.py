'''
Print all pairs in an array whose sum equals a given number.
'''
arr = [1,3,4,2,5,1,3,5,7,1,4,7,1,7]
target = 8
result = []
for i in range(len(arr)-1):
    if arr[i] + arr[i+1] == target:
        result.append([arr[i],arr[i+1]])
print(result)
