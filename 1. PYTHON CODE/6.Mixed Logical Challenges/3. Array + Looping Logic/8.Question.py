'''
Find the second largest element in an array. 
'''
arr = [ 1, 2, 5, 7, 4, 9, 3, 6]
largest = arr[0]
second_largest = arr[0]
for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(f"Second Largest: {second_largest}")