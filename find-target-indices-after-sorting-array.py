class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        
        return result

mySolution = Solution()
print(mySolution.targetIndices([1,2,5,2,3], 2))