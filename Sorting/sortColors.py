# 20min
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            min = nums[i]
            j = i - 1
            while j >= 0 and min < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = min
          
        
mySolution = Solution()
print(mySolution.sortColors([2,0,2,1,1,0]))