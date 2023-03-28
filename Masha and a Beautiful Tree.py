def divideAndConquer(nums):
    if len(nums) == 1:
        return nums, 0
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return [nums[1], nums[0]], 1
        return nums, 0
    length = len(nums) 
    left = divideAndConquer(nums[:length // 2])
    right = divideAndConquer(nums[length // 2:])
    if left[0][-1] < right[0][0]:
        return left[0] + right[0], left[1] + right[1]
    return right[0] + left[0], left[1] + right[1] + 1
     



testcases = int(input())
for _ in range(testcases):
    n = int(input())
    nums = list(map(int, input().split()))
    arr, ops = divideAndConquer(nums)
    flag = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            flag = False
            break
    if flag:
        print(ops)
    else:
        print(-1)


