N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
nums.sort()
for i in range(len(nums)):
    print(nums[i])