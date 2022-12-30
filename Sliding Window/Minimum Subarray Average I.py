#time 20
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        windowEnd = k - 1
        windowStart = 0
        maxAverage = -(10**4)
        windowSum = sum(nums[windowStart:windowEnd])
        while windowEnd < len(nums):
            windowSum += nums[windowEnd]
            avg = windowSum/(windowEnd - windowStart + 1)
            maxAverage = max(avg, maxAverage)
            windowSum -= nums[windowStart]
            windowEnd += 1
            windowStart += 1
            
        return maxAverage