class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = len(nums)
        prefixSum = [0]
        currSum = 0
        for i in range(maxLen):
            prefixSum.append(prefixSum[i] + nums[i])
        totalSum = prefixSum[-1]
        for i in range(1, maxLen+1):
            if prefixSum[i - 1] == totalSum - prefixSum[i]:
                return i-1
            
        return -1
            