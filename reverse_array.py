#revrse array
nums = [1,2,3,4,5]
n = len(nums) - 1
right = n
left = 0
temp = 0

while left < right:
    temp = nums[right]
    nums[right] = nums[left]
    nums[left] = temp
    left += 1
    right -= 1

print(nums)