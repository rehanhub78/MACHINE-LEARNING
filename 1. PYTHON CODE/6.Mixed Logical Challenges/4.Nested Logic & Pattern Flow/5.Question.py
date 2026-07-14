'''
Count how many times a number appears consecutively in an array.
'''
arr = [1,1,1,2,2,3,3,3,3]
max_count = 1
current_count = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print(f"Maximum consecutive occurrences: {max_count}")