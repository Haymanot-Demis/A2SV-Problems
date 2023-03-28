class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length  = len(nums)
        pointer = 0
        while pointer < length:
            if nums[pointer] == pointer:
                nums[pointer] = -1
                pointer += 1
            elif nums[pointer] < length and nums[pointer] != -1:
                nums[nums[pointer]], nums[pointer] = -1, nums[nums[pointer]]
            else:
                pointer += 1
        
        for indx in range(len(nums)):
            if nums[indx] != -1:
                return indx
        return length