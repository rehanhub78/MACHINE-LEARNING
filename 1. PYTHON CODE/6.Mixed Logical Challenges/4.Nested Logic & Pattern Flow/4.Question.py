'''
Check if an array is sorted (ascending or descending).
'''
arr = [1,3,4,8,7,9]
isincreasing = all(arr[i]<arr[i+1] for i in range(len(arr)-1))
isdecreasing = all(arr[i]>arr[i+1] for i in range(len(arr)-1))
issorted = isincreasing or isdecreasing
print(f"Is array sorted : {issorted}")
