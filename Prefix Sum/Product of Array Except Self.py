#time 30
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1]*length
        for i in range(1, length):
            result[i] = result[i - 1] * nums[i - 1]
        
        for i in range(length - 2, -1, -1):
            result[i] *= nums[i+1]
            nums[i] *= nums[i+1]

        return result
