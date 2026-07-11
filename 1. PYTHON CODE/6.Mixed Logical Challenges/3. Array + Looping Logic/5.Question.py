'''
Shift all zeros to the end of the array.
'''
arr = [1,0,0,2,0,2,3,0,0,4,0,5,0]
j=0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j],arr[i]= arr[i],arr[j]
        j += 1
print(arr)
