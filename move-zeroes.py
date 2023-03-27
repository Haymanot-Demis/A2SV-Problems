class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLength = len(nums)
        left = 0
        right = 0
        while left < numsLength:
            while left < numsLength and nums[left] != 0:
                left += 1
            if left == numsLength:
                break
            right = left + 1
            while right < numsLength and nums[right] == 0:
                right += 1
            if right == numsLength:
                break
            nums[left], nums[right] = nums[right], nums[left]