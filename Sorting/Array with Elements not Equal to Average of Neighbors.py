#30
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums) - 1):
            if nums[i] == (nums[i + 1] + nums[i - 1])/2:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                self.checkBack(nums, i - 1)

        return nums
        
    def checkBack(self, nums: list[int], i:int):
        if i != 0 and nums[i] == (nums[i + 1] + nums[i - 1])/2:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                self.checkBack(nums, i - 1)