nums = [2, 7, 11, 15]
target = 9
answer = []
left = 0
right = len(nums)-1
while left < right:
    if nums[left] + nums[right] < target:
        left += 1
    elif nums[left] + nums[right] > target:
        right -= 1
    else:
        answer.append(left)
        answer.append(right)
        break
print(answer)
