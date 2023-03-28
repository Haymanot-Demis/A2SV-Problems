class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length  = len(nums) + 1
        nums.append(length)
        i = 0
        while i < length:
            if nums[i] != i and nums[i] != length:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
            else:
                i += 1
        return nums.index(length)