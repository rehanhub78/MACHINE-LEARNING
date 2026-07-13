'''
Print all subarrays of a given array.
'''
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
for i in range(n):
    for j in range(i, n):
        print(arr[i:j+1],",", end=" ")
print()