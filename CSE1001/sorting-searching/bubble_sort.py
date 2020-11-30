nums = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    nums.append(int(input()))

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
print('-------------------After bubble sort----------------')
for i in nums:
    print(i)
