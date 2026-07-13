'''
Find the sum of all elements at odd indexes.
'''
arr = [ 1, 2, 5, 7, 4, 9, 3, 6]
sum = 0
for i in range(1,len(arr),2):
    sum += arr[i]
print(f"The sum of all elements at odd indexes : {sum}")