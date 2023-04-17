class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        indx = 0
        while indx < len(nums):
            if indx == nums[indx] - 1 or not nums[indx]:
                nums[indx] = 0
                indx += 1
            elif nums[indx] and nums[nums[indx] - 1]:
                nums[nums[indx] - 1], nums[indx] = 0, nums[nums[indx] - 1]
            else:
                return nums[indx]