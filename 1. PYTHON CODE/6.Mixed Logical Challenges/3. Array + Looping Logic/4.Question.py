'''
Reverse an array in-place.
'''
arr = [1,2,3,4,5,6,7,8,9,0]
for i in range(len(arr)//2):
    temp = arr[i]
    arr[i]= arr[len(arr)-1-i]
    arr[len(arr)-1-i] = temp
print(arr)
