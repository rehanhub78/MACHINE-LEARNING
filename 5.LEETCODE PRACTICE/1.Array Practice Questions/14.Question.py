nums = [-2, 1, -3, 4, -1, 2, 1, -5]
max_sum = nums[0]
curr_sum = nums[0]
for i in range(1, len(nums)):
    curr_sum += nums[i]
    if curr_sum < nums[i]:
        curr_sum = nums[i]
    elif curr_sum > max_sum:
        max_sum = curr_sum
        
print(max_sum)