'''
Find common elements between two arrays.
'''
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
common_elements = [x for x in arr1 if x in arr2]
print("Common elements:", common_elements)