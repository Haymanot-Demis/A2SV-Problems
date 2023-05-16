class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] != pointer + 1 and 1 <= nums[pointer] <= len(nums) and nums[pointer] != nums[nums[pointer] - 1]:
                temp = nums[pointer]
                nums[pointer], nums[temp - 1] = nums[temp - 1], temp
            else:
                pointer += 1
            
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1