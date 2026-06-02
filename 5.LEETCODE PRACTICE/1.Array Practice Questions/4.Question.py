nums = [1, 2, 3, 4, 5]
for i in range(len(nums)//2):
    nums[i] , nums[len(nums)-1-i] = nums[len(nums)-1-i] , nums[i]

print(nums)