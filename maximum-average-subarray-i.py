class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowEnd = k - 1
        windowStart = 0
        maxSum = -float("inf")
        windowSum = sum(nums[windowStart:windowEnd])
        while windowEnd < len(nums):
            windowSum += nums[windowEnd]
            maxSum = max(windowSum, maxSum)
            windowSum -= nums[windowStart]
            windowEnd += 1
            windowStart += 1
            
        return maxSum/k