#time = 40
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        windowStart = 0
        windowEnd = 0
        maxLengthOfOnes = 0
        numsLen = len(nums)
        while windowStart < numsLen:
            while windowEnd < numsLen and (nums[windowEnd] > 0 or k > 0):
                if nums[windowEnd] == 0:
                    k -= 1
                windowEnd += 1
            
            maxLengthOfOnes = max(maxLengthOfOnes, windowEnd - windowStart)
            print(nums[windowStart:windowEnd])
            if nums[windowStart] == 0:
                k += 1
            windowStart += 1
        
        return maxLengthOfOnes