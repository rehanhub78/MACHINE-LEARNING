hights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area = 0
left = 0
right = len(hights)-1
while left < right:
    width = right - left
    Height = min(hights[left] , hights[right])
    area = width*Height 
    if area > max_area:
        max_area = area
    if hights[left] < hights[right]:
        left += 1
    else:
        right -= 1
print(max_area)