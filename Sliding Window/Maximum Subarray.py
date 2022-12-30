#time 80
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = -10**8
        maxSubarr = []
        left = 0
        right = 0
        Sum = 0
        while right < len(nums):
            Sum += nums[right]
            maxSum = max(Sum, maxSum)
            if nums[right] > Sum:
                Sum  = nums[right]
                left = right
                maxSum = max(Sum, maxSum)
            right += 1

        return maxSum