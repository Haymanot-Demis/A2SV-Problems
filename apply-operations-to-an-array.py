class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        index = 0
        length = len(nums)
        while index < length - 1:
            if nums[index] != 0 and nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
                index += 2
            else:
                index += 1
        left = 0
        right =  0
        while right < length:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        return nums