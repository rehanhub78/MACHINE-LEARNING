'''
Count how many elements are even at an even index.
'''
array = [1, 2, 4, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in range(0,len(array),2):
    if array[i] % 2 == 0:
        count += 1

print(f"Number of Elements are even at even index is {count}")