nums = [2, 3, 1, 2, 4, 3]
target = 7
left = 0
curr_sum = 0
min_length = len(nums) + 1
for right in range(len(nums)):
    curr_sum += nums[right]
    while curr_sum >= target:
        min_length = min( min_length, (right - left + 1))
        curr_sum -= nums[left]
        left += 1

print(min_length)