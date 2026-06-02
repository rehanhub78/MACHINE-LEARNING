nums = [1, 2, 3, 4]
j = 0
while j < len(nums):
    nums[j],nums[j+1] = nums[j+1],nums[j]
    j += 2
print(nums)

# Second method
nums = [1, 2, 3, 4]
for j in range(0,len(nums),2):
    nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)