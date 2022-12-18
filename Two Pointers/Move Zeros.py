class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLength = len(nums)
        left = numsLength - 1
        right = left
        while left >= 0:
            while left >= 0 and nums[left] != 0:
                left -= 1
            
            if left >= 0:
                right = left + 1
                while right < numsLength and nums[right] != 0:
                    nums[right - 1] = nums[right]
                    right += 1
                nums[right - 1] = 0

            left -= 1