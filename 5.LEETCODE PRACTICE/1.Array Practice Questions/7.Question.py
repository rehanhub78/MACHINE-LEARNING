nums = [3, 1, 2, 4, 5, 8, 10]
j = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums[i] , nums[j] = nums[j] , nums[i]
        j += 1

print(nums)