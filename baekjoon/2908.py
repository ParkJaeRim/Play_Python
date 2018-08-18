nums = input().split(" ")

for i in range(0,2):
    nums[i] = nums[i][::-1]
    nums[i] = int(nums[i])

if nums[0] > nums[1]:
    print(nums[0])
else:
    print(nums[1])
