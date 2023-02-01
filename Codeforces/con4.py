testcases = int(input())
for _ in range(testcases):
    length, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(length - 1):
        nums[i + 1] -= nums[i]
        nums[i] = 0
    for i in range(1, length):
        nums[i] += nums[i - 1]
    print(nums)
