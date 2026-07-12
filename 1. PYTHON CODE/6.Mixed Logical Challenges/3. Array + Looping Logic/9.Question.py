'''
Rotate an array by one position to the right.
'''
arr = [1, 2, 3, 4, 5]
temp = arr[len(arr)-1]
first = arr[0]
for i in range(len(arr)):
    if i == len(arr) - 1:
        arr[0] = temp
    else:
        first,arr[i + 1] = arr[i+1],first
print(arr)