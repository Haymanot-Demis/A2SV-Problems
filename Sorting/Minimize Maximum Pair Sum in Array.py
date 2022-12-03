#time = 5min
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxSum = 0
        for i in range(len(nums)/2):
            if maxSum < nums[i] + nums[len(nums) - i - 1]:
                maxSum = nums[i] + nums[len(nums) - i - 1]
            
        return maxSum