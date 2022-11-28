# 10
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter[i] += 1
        return counter
    
mySolution = Solution()
print(mySolution.smallerNumbersThanCurrent([8,1,2,2,3]))