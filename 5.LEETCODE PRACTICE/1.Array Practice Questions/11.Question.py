nums = [2, 1, 5, 1, 3, 2]
add = 0
for i in range(3):
    add += nums[i]
curr_sum = add
j = 3
while j < len(nums):
    add += nums[j]
    add -= nums[j-3]
    curr_sum = max(curr_sum , add)
    j += 1

print(curr_sum)
    
