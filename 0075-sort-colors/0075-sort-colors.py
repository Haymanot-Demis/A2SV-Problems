class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        hold = length - 1
        for seeker in range(length - 1, -1, -1):
            if nums[seeker] != 0:
                nums[seeker], nums[hold] = nums[hold], nums[seeker]
                hold -= 1

        hold = length - 1
        seeker = hold
        while seeker > -1 and nums[seeker] != 0:
            if nums[seeker] != 1:
                nums[seeker], nums[hold] = nums[hold], nums[seeker]
                seeker -= 1
                hold -= 1
            else:
                seeker -= 1

       
